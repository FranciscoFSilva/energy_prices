import requests

from errors import EnergyPricesFileNotFoundError


def request_omie_energy_prices(url: str) -> requests.Response:
    """request_omie_energy_prices"""
    request = requests.get(url, timeout=100)
    if request.status_code != 200:
        raise EnergyPricesFileNotFoundError(
            "Maybe there is something wrong with the filename."
        )
    return request
