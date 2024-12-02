import requests

from errors.errors import NoContentInResponseError


class EnergyPriceRequest:
    def __init__(self, url: str, decoder: str = "utf-8") -> None:
        self.url = url
        self.decoder = decoder

    def get_energy_prices(self) -> list[str]:
        with requests.get(self.url, stream=True) as response:
            response.raise_for_status()
            if not response.content:
                raise NoContentInResponseError("file is empty.")
            data = []
            for chunk in response.iter_content(chunk_size=10_240):
                data.append(chunk.decode(self.decoder))
        return data
