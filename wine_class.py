class Wine:
    def __init__(self, name, country, region, price):
        self.name = name
        self.country = country
        self.region = region
        self.update_price(price)

    def update_price(self, new_price):
        if not isinstance(new_price, (int, float)) or isinstance(new_price, bool):
            raise TypeError("Price must be a number")
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price

# Use if for independent checks
# Use elif for mutually exclusive alternatives
# Use elif when selecting between alternatives. Use separate if statements when performing separate checks. But always consider whether return or raise already stops execution.



class WineCellar:
    def __init__ (self): # __init__() must return None
        # self.wines = []
        self.wines = {} # dictionary preferred to track both wines and quantity

    # def add_wine(self, wine):
        # self.wines.append(wine)

    def add_wine(self, wine, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be a positive integer.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer number.")
        if wine not in self.wines:
            self.wines[wine] = quantity
        else:
            self.wines[wine] += quantity

    def set_quantity(self, wine, quantity):
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be a non-negative integer.")
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        if wine not in self.wines:
            raise KeyError("Wine does not exist in your cellar.")
        self.wines[wine] = quantity

    def reset_quantity(self, wine):
        if wine not in self.wines:
            raise KeyError("This wine does not exist in your cellar")
        self.set_quantity(wine, 0)
        
    def remove_wine_from_cellar(self, wine):
        if not wine in self.wines:
            raise KeyError("This wine does not exist in your cellar")
        # self.wines.pop(wine)    
        del self.wines[wine]
    # both .pop(wine) without a default and del self.wines[wine] already raise KeyError if the key doesn't exist. Your explicit check is useful if you want a custom error message, but isn't strictly necessary.
    
    def calculate_total_value(self):
        total = 0
        for wine, quantity in self.wines.items():
            total += wine.price * quantity
        return total

    def get_most_expensive_wine(self):
        most_expensive_wine = None
        max_value = 0
        for wine in self.wines:
            if wine.price > max_value or most_expensive_wine is None:
                most_expensive_wine = wine
                max_value = wine.price
        return most_expensive_wine

    def get_wines_per_country(self, country):
        wine_country = []
        for wine in self.wines:
            if wine.country.lower() == country.lower():
                wine_country.append(wine)
        return wine_country

if __name__ == "__main__":
    wine_1 = Wine("Gros Plant", "France", "Loire", 12.5)
    print(wine_1.price)
    wine_1.update_price(15)
    print(wine_1.price)
    try:
        wine_2 = Wine("Muscadet", "France", "Loire", -2)    
    except ValueError as e:
        print("Error:", e)

    try:
        wine_3 = Wine("Muscadet", "France", "Loire", "34")
    except TypeError as e:
        print("Error:", e)

# a failed update should preserve its previous state, while a failed initialization should prevent the object from being created successfully.



    cellar_1 = WineCellar()
    print(cellar_1.wines)

    my_present = Wine("Yves Cuilleron", "France", "Rhône", 4500)
    cellar_1.add_wine(my_present, 10)
    # print(cellar_1.wines) 
    # print(len(cellar_1.wines))
    # print(cellar_1.wines[0].name)
    # print(cellar_1.wines[0].region)
    # print(cellar_1.wines[0].price)
    print(cellar_1.wines[my_present])

    casual_choice = Wine("Bordeaux Supérieur", "France", "Bordeaux", 15)
    big_occasion = Wine("Cheval Blanc", "France", "Bordeaux", 32000)

    cellar_1.add_wine(big_occasion, 2)
    cellar_1.add_wine(casual_choice, 4)


    print(cellar_1.calculate_total_value())
    print(cellar_1.get_most_expensive_wine().name)


    this_great_cellar = WineCellar()
    this_great_cellar.add_wine(Wine("OZ", "Italy", "Torino", 35), 4)
    this_great_cellar.add_wine(Wine("Smo", "France", "Alsace", 45), 5)
    this_great_cellar.add_wine(Wine("HE", "South Africa", "Johannesburg", 46), 5)
    wine_selection = this_great_cellar.get_wines_per_country("italy")
    for wine in wine_selection:
        print(wine.name)

    try:
        this_great_cellar.add_wine(Wine("JKD", "Spain", "Rioja", 202), "three")
    except TypeError as e:
        print("Be careful:", e)

    try:
        this_great_cellar.add_wine(Wine("KEP", "South Africa", "Johannesburg", 45), -45)
    except ValueError as e:
        print("Let's focus here for a bit:", e)

    try:
        this_great_cellar.add_wine(Wine("LWP", "France", "Loire", 23), 0)
    except ValueError as e:
        print("Not acceotable:", e)

    