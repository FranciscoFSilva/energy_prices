import datetime_utils
import parse_utils
from energy_price_request import EnergyPriceRequest
from url_getter.url_getter import URLGetter
from url_getter.url_strategies import DailyURL


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrow_date_as_str()
    url = URLGetter(DailyURL())
    energy_price_request = EnergyPriceRequest(url.get_url(tommorows_date))
    response = energy_price_request.get_response()
    energy_prices = energy_price_request.get_energy_prices(response)

    print(parse_utils.get_portuguese_prices(energy_prices))

    response.close()


if __name__ == "__main__":
    main()
