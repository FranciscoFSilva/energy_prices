import requests

from errors import NoContentInResponseError


class EnergyPriceRequest:
    def __init__(self, url):
        self.url = url

    def get_response(self) -> requests.Response:
        response = requests.get(self.url, stream=True)
        if response.raise_for_status() is None:
            return response

    def get_energy_prices(self, response: requests.Response) -> list[str]:
        if not response.content:
            raise NoContentInResponseError("file is empty.")
        data = []
        for line in response.iter_lines():
            data.append(line.decode("utf-8"))
        return data
