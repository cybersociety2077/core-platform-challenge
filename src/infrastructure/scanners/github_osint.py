from typing import List

import requests

from src.domain.models import GithubMention

GITHUB_SEARCH_URL = "https://api.github.com/search/code"


class GithubOsintScanner:
    def scan(self, domain: str) -> List[GithubMention]:
        try:
            response = requests.get(
                GITHUB_SEARCH_URL,
                params={"q": f'"{domain}"'},
                headers={"Accept": "application/vnd.github.v3+json"},
                timeout=10,
            )
            response.raise_for_status()
            results = response.json()
        except requests.RequestException:
            return []

        mentions = []
        for item in results.get("items", [])[:10]:
            mentions.append(
                GithubMention(
                    repo=item.get("repository", {}).get("full_name", ""),
                    file=item.get("name", ""),
                    url=item.get("html_url", ""),
                )
            )

        return mentions
