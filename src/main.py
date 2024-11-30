import datetime_utils
import request
import url_utils
from errors import ContentTypeIsNotPlainTextError


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrows_datetime()
    url = url_utils.get_price_url(tommorows_date)
    r = request.request_omie_energy_prices(url)

    if request.check_content_type(r) != "text/plain":
        raise ContentTypeIsNotPlainTextError("Check if omie.es changed the file type")

    response = request.get_request_content(r)

    print(response)


if __name__ == "__main__":
    main()
