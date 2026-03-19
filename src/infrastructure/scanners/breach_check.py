from typing import List

import requests

from src.domain.models import BreachInfo

HIBP_BREACHES_URL = "https://haveibeenpwned.com/api/v3/breaches"


class BreachCheckScanner:
    def scan(self, domain: str) -> List[BreachInfo]:
        try:
            response = requests.get(HIBP_BREACHES_URL, timeout=10)
            response.raise_for_status()
            breaches = response.json()
        except requests.RequestException:
            return []

        results = []
        for breach in breaches:
            if breach.get("Domain", "").lower() == domain.lower():
                results.append(
                    BreachInfo(
                        name=breach.get("Name", ""),
                        date=breach.get("BreachDate", ""),
                        affected_accounts=breach.get("PwnCount", 0),
                    )
                )

        return results
