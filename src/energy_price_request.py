import requests

from errors.errors import NoContentInResponseError


def get_energy_prices(url, decoder) -> list[str]:
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        if not response.content:
            raise NoContentInResponseError("file is empty.")
        data = []
        for chunk in response.iter_content(chunk_size=10_240):
            data.append(chunk.decode(decoder))
    return data
