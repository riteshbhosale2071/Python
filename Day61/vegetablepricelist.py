def vegetable():
    vegetables = {
        "Potato": 30,
        "Tomato": 40,
        "Onion": 35,
        "Carrot": 50
    }

    print("Vegetable Price List\n")

    for veg, price in vegetables.items():
        print(veg, "= ₹", price, "per kg")

vegetable()