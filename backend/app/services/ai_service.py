"""AI service for vLLM integration."""

import logging
from typing import Optional
import httpx
from pydantic import BaseModel

from app.config import settings
from app.models.control import Control
from app.core.exceptions import AIServiceError

logger = logging.getLogger(__name__)


class ComplianceSuggestion(BaseModel):
    """AI compliance analysis result."""
    compliance_status: str  # COMPLIANT, PARTIAL, NON_COMPLIANT
    confidence: float
    reasoning_en: str
    reasoning_ar: str
    recommendations: list[str] = []


class AIService:
    """AI service using vLLM OpenAI-compatible API."""

    def __init__(self):
        self.base_url = settings.vllm_base_url
        self.model_name = settings.vllm_model_name
        self.max_tokens = settings.vllm_max_tokens
        self.temperature = settings.vllm_temperature

    async def analyze_evidence(self, evidence_text: str, control: Control) -> ComplianceSuggestion:
        """
        Analyze evidence against a control requirement.

        Args:
            evidence_text: The evidence content to analyze
            control: The control to check compliance against

        Returns:
            ComplianceSuggestion with analysis results
        """
        try:
            # Build system prompt
            system_prompt = self._build_system_prompt(control)

            # Build user prompt
            user_prompt = f"""
            Analyze the following evidence against the control requirement:

            Evidence:
            {evidence_text}

            Provide your analysis in JSON format with the following structure:
            {{
                "compliance_status": "COMPLIANT|PARTIAL|NON_COMPLIANT",
                "confidence": 0.0-1.0,
                "reasoning_en": "English explanation",
                "reasoning_ar": "Arabic explanation",
                "recommendations": ["recommendation1", "recommendation2"]
            }}
            """

            # Call vLLM API
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{self.base_url}/v1/chat/completions",
                    json={
                        "model": self.model_name,
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": user_prompt}
                        ],
                        "max_tokens": self.max_tokens,
                        "temperature": self.temperature,
                    }
                )

                if response.status_code != 200:
                    raise AIServiceError(f"vLLM API error: {response.status_code}")

                result = response.json()
                content = result["choices"][0]["message"]["content"]

                # Parse JSON response
                import json
                suggestion_data = json.loads(content)
                return ComplianceSuggestion(**suggestion_data)

        except httpx.HTTPError as e:
            logger.error(f"HTTP error calling vLLM: {e}")
            raise AIServiceError(f"Failed to connect to AI service: {e}")
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse AI response: {e}")
            raise AIServiceError("AI service returned invalid response")
        except Exception as e:
            logger.error(f"AI service error: {e}")
            raise AIServiceError(f"AI analysis failed: {e}")

    def _build_system_prompt(self, control: Control) -> str:
        """Build system prompt with control context."""
        return f"""
        You are an expert GRC (Governance, Risk, and Compliance) auditor specializing in Saudi Arabian regulatory frameworks.
        Your task is to analyze evidence documents to determine compliance with specific control requirements.

        Control Information:
        - ID: {control.control_id}
        - Domain (English): {control.domain_en}
        - Domain (Arabic): {control.domain_ar}
        - Title (English): {control.title_en}
        - Title (Arabic): {control.title_ar}
        - Requirement (English): {control.description_en}
        - Requirement (Arabic): {control.description_ar}

        Instructions:
        1. Carefully analyze the provided evidence against the control requirement
        2. Determine if the evidence demonstrates compliance (COMPLIANT), partial compliance (PARTIAL), or non-compliance (NON_COMPLIANT)
        3. Provide a confidence score (0.0-1.0) indicating how certain you are of your assessment
        4. Explain your reasoning in both English and Arabic
        5. Provide specific recommendations if the evidence is not fully compliant

        Be objective, thorough, and cite specific elements from the evidence in your reasoning.
        """
