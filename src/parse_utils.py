def parse_energy_prices(response_str: str) -> str:
    data = response_str.replace("\n", "")
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
