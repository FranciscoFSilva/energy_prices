from url_getter.url_interface import URL


class StorageURL(URL):
    def get_url(self, date_str):
        return (
            "https://www.omie.es/pt/file-download"
            + "?parents[0]=marginalpdbcpt"
            + "&filename=marginalpdbcpt_"
            + date_str
            + ".1"
        )


class DailyURL(URL):
    def get_url(self, date_str):
        year = date_str[0:4]
        month = date_str[4:6]
        day = date_str[6::]
        return (
            "https://www.omie.es/sites/default/files/dados/"
            + "AGNO_"
            + year
            + "/MES_"
            + month
            + "/TXT/INT_PBC_EV_H_1_"
            + "_".join((day, month, year))
            + "_"
            + "_".join((day, month, year))
            + ".TXT"
        )
