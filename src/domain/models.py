from pydantic import BaseModel
from typing import Any, List


class DescribedField(BaseModel):
    value: Any
    description: str


class BreachInfo(BaseModel):
    name: str
    date: str
    affected_accounts: int


class CertificateInfo(BaseModel):
    subdomain: str


class EmailSecurityAnalysis(BaseModel):
    mail_servers: DescribedField
    spf_record: DescribedField
    dmarc_record: DescribedField
    has_spf_protection: DescribedField
    has_dmarc_protection: DescribedField


class GithubMention(BaseModel):
    repo: str
    file: str
    url: str


class GoogleDork(BaseModel):
    description: str
    url: str


class CyberIntelligenceResult(BaseModel):
    domain: str
    breaches: List[BreachInfo]
    certificates: List[CertificateInfo]
    email_security: EmailSecurityAnalysis
    github_mentions: List[GithubMention]
    google_dorks: List[GoogleDork]
