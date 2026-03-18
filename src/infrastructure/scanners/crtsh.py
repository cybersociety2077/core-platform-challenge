from typing import List

import requests

from src.domain.models import CertificateInfo

CRTSH_URL = "https://crt.sh/"


class CrtshScanner:
    def scan(self, domain: str) -> List[CertificateInfo]:
        try:
            response = requests.get(
                CRTSH_URL,
                params={"q": f"%.{domain}", "output": "json"},
                timeout=15,
            )
            response.raise_for_status()
            certs = response.json()
        except (requests.RequestException, ValueError):
            return []

        subdomains = set()
        for cert in certs:
            name_value = cert.get("name_value", "")
            for name in name_value.split("\n"):
                name = name.strip().lower()
                if name and "*" not in name:
                    subdomains.add(name)

        return [CertificateInfo(subdomain=s) for s in sorted(subdomains)]
