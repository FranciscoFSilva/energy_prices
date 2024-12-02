from url.builder import URLBuilder
from url.director import URLDirector

url_dir = URLDirector(URLBuilder())


def get(type: str, date: str) -> str:
    match type:
        case "plot":
            return url_dir.build_plot_url(date)
        case "storage":
            return url_dir.build_storage_url(date)
