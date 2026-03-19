from dataclasses import dataclass

from src.domain.models import CyberIntelligenceResult
from src.infrastructure.scanners.breach_check import BreachCheckScanner
from src.infrastructure.scanners.crtsh import CrtshScanner
from src.infrastructure.scanners.dns_analysis import DnsScanner
from src.infrastructure.scanners.github_osint import GithubOsintScanner
from src.infrastructure.scanners.google_dorks import GoogleDorksScanner


@dataclass
class CyberIntelligenceInput:
    domain: str


class CyberIntelligence:
    def __init__(self):
        self.breach_scanner = BreachCheckScanner()
        self.crtsh_scanner = CrtshScanner()
        self.dns_scanner = DnsScanner()
        self.github_scanner = GithubOsintScanner()
        self.dorks_scanner = GoogleDorksScanner()

    def __call__(self, data: CyberIntelligenceInput) -> CyberIntelligenceResult:
        domain = data.domain

        breaches = self.breach_scanner.scan(domain)
        certificates = self.crtsh_scanner.scan(domain)
        email_security = self.dns_scanner.scan(domain)
        github_mentions = self.github_scanner.scan(domain)
        google_dorks = self.dorks_scanner.scan(domain)

        return CyberIntelligenceResult(
            domain=domain,
            breaches=breaches,
            certificates=certificates,
            email_security=email_security,
            github_mentions=github_mentions,
            google_dorks=google_dorks,
        )
