from typing import List
from urllib.parse import quote

from src.domain.models import GoogleDork


class GoogleDorksScanner:
    def scan(self, domain: str) -> List[GoogleDork]:
        dorks = [
            {
                "description": f"Pastes con el dominio {domain}",
                "query": f'site:pastebin.com "{domain}"',
            },
            {
                "description": f"Credenciales expuestas de {domain}",
                "query": f'"{domain}" password OR secret OR token',
            },
            {
                "description": f"Tableros Trello públicos de {domain}",
                "query": f'site:trello.com "{domain}"',
            },
            {
                "description": f"Archivos de configuración de {domain}",
                "query": f"inurl:{domain} ext:env OR ext:yml OR ext:config",
            },
        ]

        return [
            GoogleDork(
                description=d["description"],
                url=f"https://www.google.com/search?q={quote(d['query'])}",
            )
            for d in dorks
        ]
