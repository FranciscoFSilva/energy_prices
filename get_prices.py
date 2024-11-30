"""modules"""


def get_datetime_as_str(date: datetime) -> str:
    """get_datetime_as_str"""
    return date.strftime("%d_%m_%Y")


from datetime import datetime, timedelta

import pandas as pd
import requests


class EnergyPricesFileNotFoundError(Exception):
    """Exception Class"""


class ContentTypeIsNotPlainTextError(Exception):
    """Exception Class"""


def get_previous_date(no_of_days: int) -> datetime:
    """get_previous_date"""
    return datetime.today() - timedelta(days=no_of_days)


def get_tomorrows_date() -> datetime:
    """get_tomorrows_date"""
    return datetime.today() + timedelta(days=1)


def request_omie_energy_prices(date: datetime) -> requests.Response:
    """request_omie_energy_prices"""
    date_as_str = get_datetime_as_str(date)
    request = requests.get(
        "https://www.omie.es/sites/default/files/dados/AGNO_"
        + str(date.year)
        + "/MES_"
        + str(date.month)
        + "/TXT/INT_PBC_EV_H_1_"
        + date_as_str
        + "_"
        + date_as_str
        + ".TXT",
        timeout=100,
    )
    return request


def get_datetime_as_str(date: datetime) -> str:
    """get_datetime_as_str"""
    return date.strftime("%d_%m_%Y")


def save_energy_prices(request: requests.Response) -> None:
    """save_energy_prices"""
    if request.headers["content-type"] != "text/plain":
        raise ContentTypeIsNotPlainTextError("Check if omie.es changed the file type")
    with open("energy_prices.txt", "w", encoding="UTF-8") as file:
        file.write(request.text)


def get_portuguese_prices_from_energy_prices() -> str:
    """get_portuguese_prices_from_energy_prices"""
    with open("energy_prices.txt", "r", encoding="UTF-8") as file:
        data = file.read().replace("\n", "")
        start_index = data.rfind("Precio marginal en el sistema portugués (EUR/MWh);")
        end_index = data.find("Energía total de compra sistema español (MWh)")
        energy_prices = (
            data[start_index:end_index]
            .removeprefix("Precio marginal en el sistema portugués (EUR/MWh);")
            .replace(",", ".")
            .replace(" ", "")
            .replace(";", "\n")
        )[:-1]
    return energy_prices


r = request_omie_energy_prices(get_tomorrows_date())
save_energy_prices(r)
energy_prices = get_portuguese_prices_from_energy_prices()

with open("energy_prices_portugal.csv", "w", encoding="UTF-8") as file:
    file.write(energy_prices)

df = pd.read_csv("energy_prices_portugal.csv", header=None)
df = df.rename(columns={0: "Energy Price [EUR/MWh]"})
df.index = df.index
df.index.name = "hours"
with pd.ExcelWriter("final_energy_prices.xlsx", mode="a") as writer:
    work_book = writer.book
    try:
        work_book.remove(work_book["omie_pt_prices"])
    except:
        print("Worksheet does not exist")
    finally:
        df.to_excel(writer, sheet_name="omie_pt_prices")
