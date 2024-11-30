import datetime_utils
import errors
import request
import url_utils


def main() -> None:
    tommorows_date = datetime_utils.get_tomorrows_datetime()
    url = url_utils.get_price_url(tommorows_date)
    r = request.request_omie_energy_prices(url)

    if r.status_code != 200:
        raise errors.EnergyPricesFileNotFoundError(
            "Maybe there is something wrong with the filename."
        )

    if r.headers["content-type"] != "text/plain":
        raise errors.ContentTypeIsNotPlainTextError(
            "Check if omie.es changed the file type"
        )

    response = r.text

    print(response)


if __name__ == "__main__":
    main()
