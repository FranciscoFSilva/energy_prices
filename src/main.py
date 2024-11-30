import datetime_utils
import request
import url_utils


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrows_datetime()
    url = url_utils.get_price_url(tommorows_date)
    r = request.request_omie_energy_prices(url)
    print(r)


if __name__ == "__main__":
    main()
