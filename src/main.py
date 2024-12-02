import utils.datetime_utils as datetime_utils
from request.energy_price_request import EnergyPriceRequest
from request.url_builder import URLBuilder
from request.url_director import URLDirector


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrow_date_as_str()
    url_director = URLDirector(URLBuilder())
    url = url_director.build_plot_url(tommorows_date)
    energy_price_request = EnergyPriceRequest(url, "latin-1")
    energy_prices = energy_price_request.get_energy_prices()

    print(energy_prices)


if __name__ == "__main__":
    main()
