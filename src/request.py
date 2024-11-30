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


def check_content_type(response: requests.Response) -> str:
    return response.headers["content-type"]


def get_request_content(response: requests.Response) -> str:
    return response.text
