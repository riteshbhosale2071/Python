def create():
    total = 0

    while True:

        item = input("Enter item name (or exit): ")

        if item == "exit":
            break

        price = int(input("Enter item price: "))

        total += price

    print("Total Bill =", total)

create()