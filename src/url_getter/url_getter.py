from url_getter.url_interface import URL


class URLGetter:
    def __init__(self, url: URL) -> None:
        self._url = url

    @property
    def url(self) -> URL:
        return self._url

    @url.setter
    def strategy(self, url: URL) -> None:
        self._url = url

    def get_url(self, date_str: str) -> str:
        return self._url.get_url(date_str)
