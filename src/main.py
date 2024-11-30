import datetime_utils
from energy_price_request import EnergyPriceRequest
from omie_url import OmieURL


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrow_date_as_str()
    omie = OmieURL(tommorows_date)
    energy_price_request = EnergyPriceRequest(omie.url, omie.payload())
    response = energy_price_request.get_response()
    energy_prices = energy_price_request.get_energy_prices(response)

    print(energy_prices)


if __name__ == "__main__":
    main()
