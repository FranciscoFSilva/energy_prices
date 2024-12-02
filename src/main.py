import utils.datetime_utils as datetime_utils
import utils.parse_utils as parse_utils
from request.energy_price_request import EnergyPriceRequest
from request.url_getter import URLGetter
from request.url_strategies import DailyURL


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
