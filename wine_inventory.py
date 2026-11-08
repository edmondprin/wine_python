'''
WINE INVENTORY MANAGER

1. Add wine
2. View inventory
3. Calculate inventory value
4. Exit
'''

# Create a dictionary representing an initially empty inventory, then write the code needed to add a wine with its quantity and unit price.
# name, vintage, country, region, appellation, grapes, price:
inventory = {}

def add_wine(name, vintage, price, country, region, appellation, grapes):
    if name not in inventory:
            # Add the vintage and its information here
        inventory[name] = {}
        inventory[name]["vintage"] = vintage
        inventory[name]["price"] = price
        inventory[name]["country"] = country
        inventory[name]["region"] = region
        inventory[name]["appellation"] = appellation
        inventory[name]["grapes"] = grapes
# name is used as a key to access the inner dictionary
# The difference is that name is a variable, while "name" is a string literal.
# inventory[name] = {} is equivalent to inventory["Château de Pez"] = {}
        

    # Add the vintage and its information here


def get_wine_price(name):
    if name in inventory:
        return inventory[name]["price"]
    return None # no need for else as return immediately exits the function.

def update_wine_price(name, new_price):
    if name in inventory:
        inventory[name]["price"] = new_price
        return True
    return False

def get_wines_names(cellar):
    return list(cellar.keys())
    # return list(cellar)
    # return [key for key in cellar]
    # names = []
    # for k in cellar.keys():
    #     names.append(k)
    # return names

def calculate_cellar_value(cellar):
    total_value = 0
    for wine in cellar.values():
        total_value += wine["price"]
    return total_value

def get_most_expensive_wine(cellar):
    most_expensive_name = None
    highest_value = 0
    for name, wine in cellar.items():
        if wine["price"] > highest_value or most_expensive_name is None:
            highest_value = wine["price"]
            most_expensive_name = name
    return most_expensive_name

def get_wines_by_country(cellar, country):
    wines = []
    for name, wine in cellar.items():
        if wine["country"].lower() == country.lower():
            wines.append(name)
    return wines

        

if __name__ == "__main__":

    add_wine("Château de Pez", 2019, 250, "France", "Bordeaux", "Saint-Estèphe", ["cabernet sauvignon", "merlot", "cabernet franc"])
    add_wine("Michel Ogier", 2015, 34300, "France", "Rhône", "Côte-Rôtie", ['syrah'])
    add_wine("François Jobard", 1999, 2200, "France", "Bourgogne", "Meursault", ["chardonnay"])

    print(inventory)

    print(get_wine_price("François Jobard"))
    # print(inventory["wine #"]["appellation"])

    print(get_wine_price("Romanée-Conti"))

    update_wine_price("François Jobard", 3500)
    print(inventory["François Jobard"]["price"])

    print(get_wines_names(inventory))

    print(calculate_cellar_value(inventory))

    print(get_most_expensive_wine(inventory))
    print(get_most_expensive_wine({}))

    austin_cellar = {
        "Merlot": {"price": 0},
        "Chardonnay": {"price": 0}
    }

    print(get_most_expensive_wine(austin_cellar))
    
    int_cellar = {
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

    print(get_wines_by_country(int_cellar, "FRANCE"))
    print(get_wines_by_country(int_cellar, "italy"))
    print(get_wines_by_country(int_cellar, "Spain"))
