from wine_class import Wine, WineCellar
import pytest

# decorator supplies two arguments to the function
@pytest.mark.parametrize(
    "new_price, expected_exception",
    [
        ("+5%", TypeError),
        (True, TypeError),
        (-32, ValueError),
        ]
)

# One test function, three independently reported pytest cases.
def test_update_price_invalid(new_price, expected_exception):
    wine = Wine("PWD", "France", "Bordeaux", 34)

    with pytest.raises(expected_exception):
        wine.update_price(new_price)

    assert wine.price == 34


# Fixture providing fresh cellar to each test
@pytest.fixture
def cellar():
    return WineCellar()

def test_calculate_total_value_empty(cellar):
    assert cellar.calculate_total_value() == 0

@pytest.fixture
def stocked_cellar():
    cellar = WineCellar()
    wine = Wine("Muscadet", "France", "Loire", 12)
    cellar.add_wine(wine, 3)
    return cellar, wine

def test_reset_quantity_valid(stocked_cellar):
    cellar, wine = stocked_cellar
    cellar.reset_quantity(wine)
    assert cellar.wines[wine] == 0

