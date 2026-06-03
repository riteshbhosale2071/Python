def toy():
    inventory = {
        "Car": 10,
        "Doll": 15,
        "Ball": 20,
        "Robot": 5
    }

    print("Available Toys:\n")

    for toy, qty in inventory.items():
        print(toy, ":", qty)

    toy = input("\nEnter toy name: ").capitalize()

    if toy in inventory:
        print("Stock Available =", inventory[toy])

    else:
        print("Toy not found")

toy()