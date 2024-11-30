class OmieURL:
    def __init__(self, date_str):
        self.date_str: date_str
        self.url = "https://www.omie.es/pt/file-download"
        self.payload: dict = {
            "parents[0]": "marginalpdbcpt",
            "filename": "marginalpdbcpt_" + date_str + ".1",
        }
