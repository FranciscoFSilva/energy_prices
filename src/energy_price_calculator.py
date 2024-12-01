class EnergyPriceCalculator:
    def get_loss_factor():
        pass

    def get_energy_price(
        kwh_price: list[float],
        retailer_tarif: float,
        loss_factor: list[float],
        grid_access_tarif: float,
    ) -> list[float]:
        energy_price = [x + retailer_tarif for x in kwh_price]
        energy_price = map(
            lambda x, y: x * y, energy_price, [x + 1 for x in loss_factor]
        )
        energy_price = [x + grid_access_tarif for x in energy_price]
        energy_price = [round(x, 4) for x in energy_price]
        return energy_price
