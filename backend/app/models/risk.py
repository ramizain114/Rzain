"""Risk model for risk register."""

from datetime import datetime
from enum import Enum
from typing import Optional
from beanie import Document, Indexed, Link
from pydantic import Field

from app.models.user import User


class RiskLevel(str, Enum):
    """Risk severity level."""
    VERY_LOW = "VERY_LOW"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class RiskTreatment(str, Enum):
    """Risk treatment strategy."""
    ACCEPT = "ACCEPT"
    MITIGATE = "MITIGATE"
    TRANSFER = "TRANSFER"
    AVOID = "AVOID"


class Risk(Document):
    """Risk register entry."""

    risk_id: Indexed(str, unique=True)  # type: ignore
    title_en: str
    title_ar: str
    description_en: str
    description_ar: str
    asset: str  # Asset at risk
    threat: str  # Threat source
    vulnerability: str  # Vulnerability exploited
    impact_score: int = Field(ge=1, le=5)  # 1-5 scale
    likelihood_score: int = Field(ge=1, le=5)  # 1-5 scale
    risk_score: int = Field(ge=1, le=25)  # Impact × Likelihood
    risk_level: RiskLevel
    treatment: RiskTreatment = RiskTreatment.MITIGATE
    treatment_plan: Optional[str] = None
    status: str = "OPEN"  # OPEN, MONITORING, CLOSED
    owner: Link[User]
    review_date: Optional[datetime] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "risks"
        indexes = [
            "risk_id",
            "risk_level",
            "status",
        ]

    def calculate_risk_score(self) -> None:
        """Calculate risk score and level based on impact and likelihood."""
        self.risk_score = self.impact_score * self.likelihood_score

        # Determine risk level based on score
        if self.risk_score <= 3:
            self.risk_level = RiskLevel.VERY_LOW
        elif self.risk_score <= 6:
            self.risk_level = RiskLevel.LOW
        elif self.risk_score <= 12:
            self.risk_level = RiskLevel.MEDIUM
        elif self.risk_score <= 20:
            self.risk_level = RiskLevel.HIGH
        else:
            self.risk_level = RiskLevel.CRITICAL

    class Config:
        json_schema_extra = {
            "example": {
                "risk_id": "RISK-2024-001",
                "title_en": "Unauthorized Access to Database",
                "title_ar": "وصول غير مصرح به إلى قاعدة البيانات",
                "asset": "Production Database",
                "threat": "External Attacker",
                "vulnerability": "Weak Authentication",
                "impact_score": 5,
                "likelihood_score": 3,
                "risk_score": 15,
                "risk_level": "HIGH",
                "treatment": "MITIGATE",
                "status": "OPEN",
            }
        }
