from fastapi import APIRouter

from src.domain.models import CyberIntelligenceResult
from src.interfaces.schemas import CyberIntelligenceRequest
from src.use_cases.cyber_intelligence import CyberIntelligence, CyberIntelligenceInput

router = APIRouter(prefix="/security", tags=["security"])


@router.post("/cyber-intelligence", response_model=CyberIntelligenceResult)
def cyber_intelligence(body: CyberIntelligenceRequest):
    use_case = CyberIntelligence()
    result = use_case(CyberIntelligenceInput(domain=body.domain))
    return result


@router.get("/cyber-intelligence/categories")
async def cyber_intelligence_categories():
    return {
        "categories": [
            "breaches",
            "certificates",
            "dns",
            "github_mentions",
            "google_dorks",
        ]
    }
