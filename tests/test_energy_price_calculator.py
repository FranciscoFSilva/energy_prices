import pytest

from energy_price_calculator import EnergyPriceCalculator


@pytest.mark.parametrize(
    "kwh_price_list, loss_factor_list, retailer_tarif, grid_access_tarif, expected",
    [
        ([0], [0], 0, 0, [0]),
        ([0, 1, 2], [0, 1, 2], 1, 1, [2, 5, 10]),
        ([0, 0, 0, 0, 0], [1, 1, 1, 1, 1], 1, 1, [3, 3, 3, 3, 3]),
        (
            [0.23, 0.34, 0.5, 0.4],
            [0.02, 0.04, 0.01, 0.02],
            0.026,
            -0.023,
            [0.2381, 0.3576, 0.5083, 0.4115],
        ),
    ],
)
def test_get_energy_price(
    kwh_price_list: list[float],
    loss_factor_list: list[float],
    retailer_tarif: float,
    grid_access_tarif: float,
    expected: list[float],
) -> None:
    energy_prices = EnergyPriceCalculator(
        kwh_price_list, loss_factor_list, retailer_tarif, grid_access_tarif
    )
    assert energy_prices.get_energy_price() == expected
