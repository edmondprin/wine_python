from wine_inventory import get_most_expensive_wine, get_wines_by_country

def test_get_most_expensive_several_wines():
    my_cellar = {"Gros Plant":{"price": 6.5},"Cheval Blanc": {"price": 25000}, "Bordeaux Supérieur": {"price": 8}}
    result = get_most_expensive_wine(my_cellar)
    expected = "Cheval Blanc"
    assert result == expected

def test_get_most_expensive_empty_cellar():
    my_cellar = {}
    result = get_most_expensive_wine(my_cellar)
    expected = None
    assert result == expected

def test_get_most_expensive_free_wines():
    my_cellar = {"Merlot": {"price": 0}, "Anjou": {"price": 0}, "Gros Plant": {"price": 0}}
    result = get_most_expensive_wine(my_cellar)
    expected = "Merlot"
    assert result == expected

cellar = {
     "Château de Pez": {
        "country": "France",
        "region": "Bordeaux",
        "price": 250
    },
    "François Jobard": {
        "country": "France",
        "region": "Bourgogne",
        "price": 2200
    },
    "Opus One": {
        "country": "USA",
        "region": "Napa Valley",
        "price": 450
    },
    "Sassicaia": {
        "country": "Italy",
        "region": "Tuscany",
        "price": 350
    }
}

def test_get_wine_per_country_two():
    result = get_wines_by_country(cellar, "FRANCE")
    expected = ["Château de Pez", "François Jobard"]
    assert result == expected

def test_get_wine_per_country_one_upper():
    result = get_wines_by_country(cellar, "USA")
    expected = ["Opus One"]
    assert result == expected

def test_get_wine_per_country_one_lower():
    result = get_wines_by_country(cellar, "italy")
    expected = ["Sassicaia"]
    assert result == expected

def test_get_wine_per_country_no_wine():
    result = get_wines_by_country(cellar, "Chile")
    expected = []
    assert result == expected

def test_get_wine_per_country_empty():
    result = get_wines_by_country({}, "France")
    expected = []
    assert result == expected