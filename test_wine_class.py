from wine_class import Wine, WineCellar
import pytest

# Test the method (update price)

def test_update_price_valid_positive():
    wine_1 = Wine("Bordeaux", "France", "Bordeaux", 20)
    wine_1.update_price(22)
    assert wine_1.price == 22

def test_update_price_valid_zero():
    wine_1 = Wine("Muscadet", "France", "Loire", 4.5)
    wine_1.update_price(0)
    assert wine_1.price == 0

def test_update_price_invalid_str():
    wine_1 = Wine("Bordeaux", "France", "Bordeaux", 20)
    with pytest.raises(TypeError):
        wine_1.update_price("+5%")
    assert wine_1.price == 20

def test_update_price_invalid_bool():
    wine_1 = Wine("Muscadet","France", "Loire", 10)
    with pytest.raises(TypeError):
        wine_1.update_price(True)
    assert wine_1.price == 10

def test_update_price_invalid_negative():
    wine_1 = Wine("Bordeaux", "France", "Bordeaux", 20)
    with pytest.raises(ValueError):
        wine_1.update_price(-32)
    assert wine_1.price == 20

# Test the constructor (Object initialization)

def test_constructor_valid_positive():
    wine_1 = Wine("Monte Cristo", "Spain", "Rioja", 25)
    assert wine_1.name == "Monte Cristo"
    assert wine_1.country == "Spain"
    assert wine_1.region == "Rioja"
    assert wine_1.price == 25

def test_constructor_valid_zero():
    wine_1 = Wine("Monte Cristo", "Spain", "Rioja", 0)
    assert wine_1.name == "Monte Cristo"
    assert wine_1.country == "Spain"
    assert wine_1.region == "Rioja"
    assert wine_1.price == 0

# No need to assign an object because there is no assignment when the constructor raises an exception

def test_constructor_invalid_str():
    with pytest.raises(TypeError):
        Wine("Monte Cristo", "Spain", "Rioja", "thirty")

def test_constructor_invalid_bool():
    with pytest.raises(TypeError):
        Wine("Monte Cristo", "Spain", "Rioja", False)

def test_constructor_invalid_negative():
    with pytest.raises(ValueError):
        Wine("Monte Cristo", "Spain", "Rioja", -23)

def test_add_wine_valid():
    wine_1 = Wine("Bordeaux Sup", "France", "Bordeaux", 35)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 2)
    my_cellar.add_wine(wine_1, 5)
    assert my_cellar.wines[wine_1] == 7
    assert len(my_cellar.wines) == 1

# The key distinction is between an object's identity and its attributes. Two objects can have identical attributes without being the same object.

def test_add_wine_invalid_str():
    my_cellar = WineCellar()
    with pytest.raises(TypeError):
        my_cellar.add_wine(Wine("LED", "Portugal", "Lisboa", 34), "two")

def test_add_wine_invalid_zero():
    my_cellar = WineCellar()
    with pytest.raises(ValueError):
        my_cellar.add_wine(Wine("KWE", "USA", "California", 45), 0)

def test_add_wine_invalid_negative():
    my_cellar = WineCellar()
    wine_1 = Wine("KWE", "France", "Loire", 12)
    my_cellar.add_wine(wine_1, 4)
    with pytest.raises(ValueError):
        my_cellar.add_wine(wine_1, -4)
    assert my_cellar.wines[wine_1] == 4

def test_calculate_total_value_postive():
    wine_1 = Wine("Pomerol", "France", "Bordeaux", 2400)
    wine_2 = Wine("Muscadet", "France", "Loire", 25)
    wine_3 = Wine("Riesling", "France", "Alsace", 45)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 2)
    my_cellar.add_wine(wine_2, 5)
    my_cellar.add_wine(wine_3, 10)
    assert my_cellar.calculate_total_value() == 5375

def test_calculate_total_value_empty():
    my_cellar = WineCellar()
    assert my_cellar.calculate_total_value() == 0

def test_get_most_expensive_wine_valid_positive():
    wine_1 = Wine("Pomerol", "France", "Bordeaux", 2400)
    wine_2 = Wine("Muscadet", "France", "Loire", 25)
    wine_3 = Wine("Riesling", "France", "Alsace", 45)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 1)
    my_cellar.add_wine(wine_2, 1)
    my_cellar.add_wine(wine_3, 1)
    result = my_cellar.get_most_expensive_wine()
    assert result is wine_1

def test_get_most_expensive_wine_empty_cellar():
    my_cellar = WineCellar()
    assert my_cellar.get_most_expensive_wine() is None

def test_get_more_expensive_wine_same_amount():
    wine_1 = Wine("Jeanseac", "France", "Bordeaux", 15)
    wine_2 = Wine("Lansac", "France", "Champagne", 15)
    wine_3 = Wine("Oc", "France", "Roussillon", 15)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 1)
    my_cellar.add_wine(wine_2, 1)
    my_cellar.add_wine(wine_3, 1)
    assert my_cellar.get_most_expensive_wine() is wine_1

def test_get_more_expensive_wine_last():
    wine_1 = Wine("Oz", "France", "Loire", 10)
    wine_2 = Wine("HW", "Spain", "Rioja", 20)
    wine_3 = Wine("Smash", "USA", "California", 30)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 1)
    my_cellar.add_wine(wine_2, 1)
    my_cellar.add_wine(wine_3, 1)
    result = my_cellar.get_most_expensive_wine()
    assert result is wine_3

def test_get_wines_country_insensitive():
    my_cellar = WineCellar()
    wine_1 = Wine("Oz", "ITALY", "Sicilia", 340)
    wine_2 = Wine("Mae", "France", "Bordeaux", 25)
    wine_3 = Wine("Peruzzi", "iTAly", "Torino", 58)
    my_cellar.add_wine(wine_1, 1)
    my_cellar.add_wine(wine_2, 1)
    my_cellar.add_wine(wine_3, 1)
    result = my_cellar.get_wines_per_country("Italy")
    assert len(result) == 2
    assert isinstance(result, list)
    my_wines = []
    for wine in result:
        my_wines.append(wine.name)
    assert my_wines == ["Oz", "Peruzzi"]
    assert result[0] is wine_1
    assert result[1] is wine_3

def test_get_wines_country_multiple():
    my_cellar = WineCellar()
    my_cellar.add_wine(Wine("Miao", "France", "Bordeaux", 50), 1)
    my_cellar.add_wine(Wine("PWD", "UK", "Southhampton", 24), 1)
    my_cellar.add_wine(Wine("Esprit", "France", "Loire", 45), 1)
    my_cellar.add_wine(Wine("Lio", "Spain", "Rioja", 23), 1)
    my_cellar.add_wine(Wine("Pkoe", "France", "Loire", 23), 1)
    result = my_cellar.get_wines_per_country("FRANCE")
    assert len(result) == 3
    my_FR_wines = []
    for wine in result:
        my_FR_wines.append(wine.name)
    assert my_FR_wines == ["Miao", "Esprit", "Pkoe"]
    # assert "Lio" not in my_FR_wines
    # assert "PWD" not in my_FR_wines

def test_get_wines_country_empty():
    my_cellar = WineCellar()
    result = my_cellar.get_wines_per_country("France")
    assert result == []

def test_get_wines_country_unknown():
    my_cellar = WineCellar()
    my_cellar.add_wine(Wine("Ops", "Chile", "San Pedro", 34), 2)
    result = my_cellar.get_wines_per_country("Argentina")
    assert result == []

def test_set_quantity_valid():
    wine_1 = Wine("WEP", "France", "Bordeaux", 240)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 5)
    my_cellar.set_quantity(wine_1, 20)
    assert my_cellar.wines[wine_1] == 20

def test_set_quantity_zero():
    wine_1 = Wine("WDR", "France", "Bordeaux", 2023)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 25)
    assert my_cellar.wines[wine_1] == 25
    my_cellar.set_quantity(wine_1, 0)
    assert my_cellar.wines[wine_1] == 0

def test_set_quantity_invalid_str():
    wine_1 = Wine("QOP", "France", "Bordeaux", 23)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 20)
    with pytest.raises(TypeError):
        my_cellar.set_quantity(wine_1, "two hundreds")
    assert my_cellar.wines[wine_1] == 20

def test_set_quantity_invalid_negative():
    wine_1 = Wine("WDP", "France", "Loire", 23)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 35)
    with pytest.raises(ValueError):
        my_cellar.set_quantity(wine_1, -3)
    assert my_cellar.wines[wine_1] == 35

def test_set_quantity_invalid_non_existing():
    wine_1 = Wine("WDP", "France", "Loire", 23)
    my_cellar = WineCellar()
    with pytest.raises(KeyError):
        my_cellar.set_quantity(wine_1, 3)
    assert my_cellar.wines == {}

def test_reset_quantity_valid():
    wine_1 = Wine("WDP", "France", "Loire", 55)
    my_cellar = WineCellar()
    my_cellar.add_wine(wine_1, 46)
    my_cellar.reset_quantity(wine_1)
    assert my_cellar.wines[wine_1] == 0

def test_remove_existing_wine():
    wine_1 = Wine("QPK", "France", "Bourgogne", 234)
    specks = WineCellar()
    specks.add_wine(wine_1, 4)
    specks.remove_wine_from_cellar(wine_1)
    assert specks.wines == {}

def test_remove_unknown_wine():
    specks = WineCellar()
    with pytest.raises(KeyError):
        specks.remove_wine_from_cellar("wine_1")
        # specks.remove_wine_from_cellar(wine_1) would trigger NameError