def money():
    price = float(input("Enter price of one item: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity
    print("Total Amount = ₹", total)

money()