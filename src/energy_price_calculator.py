class EnergyPriceCalculator:
    def __init__(
        self,
        kwh_price: list[float],
        loss_factor: list[float],
        retailer_tarif: float,
        grid_access_tarif: float,
    ) -> None:
        self._kwh_price = kwh_price
        self._loss_factor = loss_factor
        self._retailer_tarif = retailer_tarif
        self._grid_access_tarif = grid_access_tarif

    def get_energy_price(self) -> list[float]:
        energy_price = [x + self._retailer_tarif for x in self._kwh_price]
        energy_price = map(
            lambda x, y: x * y, energy_price, [x + 1 for x in self._loss_factor]
        )
        energy_price = [x + self._grid_access_tarif for x in energy_price]
        energy_price = [round(x, 4) for x in energy_price]
        return energy_price
