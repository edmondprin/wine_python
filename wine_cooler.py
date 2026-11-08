def get_capacity():
    return input("What is the max capacity of your wine cooler? ")

def get_inventory():
    return input("How many bottles do you have in your device at the moment? ")

def get_pack_size():
    return input("How many bottles do you need to buy minimum to get a discount? ")

def verify_numbers(capacity, inventory, pack): 
    validated_numbers = [int(i) for i in (capacity, inventory, pack)] # list comprehension
    capacity, inventory, pack = validated_numbers # sequence unpacking
    if capacity <= 0 or pack <= 0: # business rule validations & exception handling
        raise ValueError("Number needs to be positive!")
    if inventory < 0:
        raise ValueError("Inventory cannot be below 0")
    if inventory > capacity:
        raise ValueError("Inventory cannot be superior to capacity")
    return validated_numbers

def calculate_max_discount_packs(capacity, inventory, pack):
    return (capacity - inventory) // pack

def format_message(number_packs, pack):
    if number_packs > 0:
        return f"You can now buy {number_packs} full pack{'s' if number_packs > 1 else ''} to get closer to filling your wine cooler!"
    else:
        return f"Not enough room at the moment to get a full pack of {pack} bottles!"

def main():
    
    while True:
        raw_capacity = get_capacity()
        raw_inventory = get_inventory()
        raw_pack = get_pack_size()
        try:
            validated_capacity, validated_inventory, validated_pack = verify_numbers(raw_capacity, raw_inventory, raw_pack) # sequence unpacking
            break
        except ValueError as e:
            print(f"Incorrect input: {e}")

    max_discount_packs = calculate_max_discount_packs(validated_capacity, validated_inventory, validated_pack) 
    message = format_message(max_discount_packs, validated_pack)
    print(message)

if __name__ == "__main__":
    main()
