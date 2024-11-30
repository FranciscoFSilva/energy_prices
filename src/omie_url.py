from dataclasses import dataclass


@dataclass
class OmieURL:
    url = "https://www.omie.es/pt/file-download"
    date_str: str

    def payload(self) -> dict:
        return {
            "parents[0]": "marginalpdbcpt",
            "filename": "marginalpdbcpt_" + self.date_str + ".1",
        }
