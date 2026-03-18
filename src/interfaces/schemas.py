from pydantic import BaseModel, HttpUrl
from typing import List


class CyberIntelligenceRequest(BaseModel):
    domain: str
