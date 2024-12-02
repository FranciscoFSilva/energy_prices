from request.url_builder import URLBuilder


class URLDirector:
    def __init__(self, builder: URLBuilder) -> None:
        self._builder = builder

    def build_storage_url(self, date_str: str) -> str:
        return (
            self._builder.set_scheme("https")
            .set_domain("www.omie.es")
            .add_path("file-download")
            .add_param("parents[0]", "marginalpdbcpt")
            .add_param("filename", "marginalpdbcpt_" + date_str + ".1")
            .build()
        )

    def build_plot_url(self, date_str: str) -> str:
        year = date_str[0:4]
        month = date_str[4:6]
        day = date_str[6::]
        date_format = "_".join((day, month, year))
        return (
            self._builder.set_scheme("https")
            .set_domain("www.omie.es")
            .add_path("sites")
            .add_path("default")
            .add_path("files")
            .add_path("dados")
            .add_path("AGNO_" + year)
            .add_path("MES" + month)
            .add_path("TXT")
            .add_path("INT_PBC_EV_H_1_" + date_format + "_" + date_format + ".TXT")
            .build()
        )
