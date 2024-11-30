import datetime_utils


def get_price_url(date: datetime_utils.datetime) -> str:
    date_as_str = datetime_utils.datetime_as_str(date)
    return (
        "https://www.omie.es/sites/default/files/dados/AGNO_"
        + str(date.year)
        + "/MES_"
        + str(date.month)
        + "/TXT/INT_PBC_EV_H_1_"
        + date_as_str
        + "_"
        + date_as_str
        + ".TXT"
    )
