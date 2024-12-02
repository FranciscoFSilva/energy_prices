from typing import Self
from urllib.parse import urlencode


class URLBuilder:
    def __init__(self) -> None:
        self.scheme = "http"
        self.domain = ""
        self.port = None
        self.path = []
        self.params = {}

    def set_scheme(self, scheme: str) -> Self:
        self.scheme = scheme
        return self

    def set_domain(self, domain: str) -> Self:
        self.domain = domain
        return self

    def set_port(self, port: int) -> Self:
        self.port = port
        return self

    def add_path(self, path: str) -> Self:
        self.path.append(path)
        return self

    def add_param(self, key: str, value: str) -> Self:
        self.params[key] = value
        return self

    def build(self) -> str:
        url = f"{self.scheme}://{self.domain}"
        if self.port:
            url += f":{self.port}"
        if self.path:
            url += f"{"/".join(self.path)}"
        if self.params:
            query_string = urlencode(self.params)
            url += f"?{query_string}"
        return url
