import requests


def request_omie_energy_prices(date: datetime) -> requests.Response:
    """request_omie_energy_prices"""
    date_as_str = get_datetime_as_str(date)
    request = requests.get(
        "https://www.omie.es/sites/default/files/dados/AGNO_"
        + str(date.year)
        + "/MES_"
        + str(date.month)
        + "/TXT/INT_PBC_EV_H_1_"
        + date_as_str
        + "_"
        + date_as_str
        + ".TXT",
        timeout=100,
    )
    if request.status_code != 200:
        raise EnergyPricesFileNotFoundError(
            "Maybe there is something wrong with the filename."
        )
    return request
