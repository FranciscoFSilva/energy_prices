from abc import ABC, abstractmethod


class URL(ABC):
    @abstractmethod
    def get_url(self, date_str) -> str:
        pass
