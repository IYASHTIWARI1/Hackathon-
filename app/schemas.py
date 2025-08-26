from pydantic import BaseModel
from typing import List, Optional

class Meta(BaseModel):
    package: str
    label: Optional[str]
    version: Optional[str]
    size_mb: float
    signer_sha256: Optional[str]
    permissions: List[str] = []
    urls: List[str] = []

class AnalysisResponse(BaseModel):
    verdict: str           # e.g., "likely_genuine", "suspicious"
    risk_score: int
    reasons: List[str]
    metadata: Meta
    sha256: str