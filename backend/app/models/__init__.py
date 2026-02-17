"""Database models (Beanie documents)."""

from app.models.user import User, Role
from app.models.standard import Standard
from app.models.control import Control, ImplementationStatus
from app.models.risk import Risk, RiskLevel, RiskTreatment
from app.models.evidence import Evidence, EvidenceStatus
from app.models.audit import Audit, AuditStatus
from app.models.nonconformity import NonConformity, Severity, NonConformityStatus

__all__ = [
    "User",
    "Role",
    "Standard",
    "Control",
    "ImplementationStatus",
    "Risk",
    "RiskLevel",
    "RiskTreatment",
    "Evidence",
    "EvidenceStatus",
    "Audit",
    "AuditStatus",
    "NonConformity",
    "Severity",
    "NonConformityStatus",
]

# List of all document models for Beanie initialization
DOCUMENT_MODELS = [
    User,
    Standard,
    Control,
    Risk,
    Evidence,
    Audit,
    NonConformity,
]
