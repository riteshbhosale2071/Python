def icecream():
    flavours = {
        "Vanilla": 30,
        "Chocolate": 40,
        "Strawberry": 35
    }

    flavour = input("Enter flavour: ").capitalize()
    quantity = int(input("Enter quantity: "))

    if flavour in flavours:

        total = flavours[flavour] * quantity

        print("Total Price = ₹", total)

    else:
        print("Flavour not available")

icecream()