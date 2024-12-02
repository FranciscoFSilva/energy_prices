def get_portuguese_prices(energy_prices: list[str]) -> list[str]:
    def parse_one_line(line: str) -> str:
        aux = line.split(";")
        date = "-".join(aux[0:3])
        hour = aux[3]
        price = aux[4]
        return ",".join([date, hour, price])

    return list(map(parse_one_line, energy_prices[1:-1]))
