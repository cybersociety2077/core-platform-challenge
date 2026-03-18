from typing import List

import dns.resolver

from src.domain.models import DescribedField, EmailSecurityAnalysis


class DnsScanner:
    def scan(self, domain: str) -> EmailSecurityAnalysis:
        mx_records = self._get_mx(domain)
        spf_record = self._get_spf(domain)
        dmarc_record = self._get_dmarc(domain)

        return EmailSecurityAnalysis(
            mail_servers=DescribedField(
                value=mx_records,
                description="Servidores encargados de recibir correo electrónico del dominio (MX Records)",
            ),
            spf_record=DescribedField(
                value=spf_record,
                description="Política que define quién puede enviar correos en nombre del dominio (SPF)",
            ),
            dmarc_record=DescribedField(
                value=dmarc_record,
                description="Política que indica qué hacer con correos que fallan validaciones SPF/DKIM (DMARC)",
            ),
            has_spf_protection=DescribedField(
                value=bool(spf_record),
                description="Indica si el dominio tiene protección SPF configurada",
            ),
            has_dmarc_protection=DescribedField(
                value=bool(dmarc_record),
                description="Indica si el dominio tiene protección DMARC configurada",
            ),
        )

    def _get_mx(self, domain: str) -> List[str]:
        try:
            answers = dns.resolver.resolve(domain, "MX")
            return [str(r.exchange).rstrip(".") for r in answers]
        except Exception:
            return []

    def _get_spf(self, domain: str) -> str:
        try:
            answers = dns.resolver.resolve(domain, "TXT")
            for r in answers:
                txt = r.to_text().strip('"')
                if txt.startswith("v=spf1"):
                    return txt
        except Exception:
            pass
        return ""

    def _get_dmarc(self, domain: str) -> str:
        try:
            answers = dns.resolver.resolve(f"_dmarc.{domain}", "TXT")
            for r in answers:
                txt = r.to_text().strip('"')
                if txt.startswith("v=DMARC1"):
                    return txt
        except Exception:
            pass
        return ""
