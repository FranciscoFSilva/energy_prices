import requests


class EnergyPriceRequest:
    def __init__(self, url, payload):
        self.url = url
        self.payload = payload

    def get_response(self) -> requests.Response:
        response = requests.get(self.url, params=self.payload, stream=True)
        if response.raise_for_status() is None:
            return response

    def get_energy_prices(self, response: requests.Response) -> str:
        data = []
        for line in response.iter_lines():
            data.append(line.decode("utf-8"))
        return "\n".join(data)
