import url
import utils.datetime_utils as datetime_utils
from energy_price_request import get_energy_prices
from errors.errors import NoContentInResponseError


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrow_date_as_str()
    try:
        energy_prices = get_energy_prices(url.get("storage", tommorows_date), "utf-8")
    except NoContentInResponseError:
        energy_prices = get_energy_prices(url.get("plot", tommorows_date), "latin-1")
    except Exception as err:
        raise err

    print("".join(energy_prices))


if __name__ == "__main__":
    main()
