"""Risk management tests."""

import pytest
from datetime import datetime

from app.models.risk import Risk, RiskLevel, RiskTreatment
from app.models.user import User, Role


@pytest.mark.asyncio
async def test_risk_score_calculation(db):
    """Test risk score and level calculation."""
    # Create a test user
    user = User(
        username="testuser",
        email="test@example.com",
        full_name_en="Test User",
        full_name_ar="مستخدم تجريبي",
        role=Role.RISK_OFFICER,
    )
    await user.insert()

    # Create risk with high impact and high likelihood
    risk = Risk(
        risk_id="RISK-TEST-001",
        title_en="Test Risk",
        title_ar="مخاطرة اختبارية",
        description_en="Test description",
        description_ar="وصف اختباري",
        asset="Test Asset",
        threat="Test Threat",
        vulnerability="Test Vulnerability",
        impact_score=5,
        likelihood_score=5,
        treatment=RiskTreatment.MITIGATE,
        owner=user,
    )

    # Calculate risk score
    risk.calculate_risk_score()

    assert risk.risk_score == 25
    assert risk.risk_level == RiskLevel.CRITICAL


@pytest.mark.asyncio
async def test_risk_level_boundaries(db):
    """Test risk level calculation for different scores."""
    user = User(
        username="testuser",
        email="test@example.com",
        full_name_en="Test User",
        full_name_ar="مستخدم تجريبي",
        role=Role.RISK_OFFICER,
    )
    await user.insert()

    test_cases = [
        (1, 1, RiskLevel.VERY_LOW),  # Score 1
        (1, 3, RiskLevel.VERY_LOW),  # Score 3
        (2, 2, RiskLevel.LOW),       # Score 4
        (2, 3, RiskLevel.LOW),       # Score 6
        (3, 3, RiskLevel.MEDIUM),    # Score 9
        (3, 4, RiskLevel.MEDIUM),    # Score 12
        (4, 4, RiskLevel.HIGH),      # Score 16
        (4, 5, RiskLevel.HIGH),      # Score 20
        (5, 5, RiskLevel.CRITICAL),  # Score 25
    ]

    for impact, likelihood, expected_level in test_cases:
        risk = Risk(
            risk_id=f"RISK-{impact}-{likelihood}",
            title_en="Test",
            title_ar="اختبار",
            description_en="Test",
            description_ar="اختبار",
            asset="Test",
            threat="Test",
            vulnerability="Test",
            impact_score=impact,
            likelihood_score=likelihood,
            treatment=RiskTreatment.ACCEPT,
            owner=user,
        )
        risk.calculate_risk_score()
        
        assert risk.risk_level == expected_level, \
            f"Impact {impact} x Likelihood {likelihood} should be {expected_level}, got {risk.risk_level}"
