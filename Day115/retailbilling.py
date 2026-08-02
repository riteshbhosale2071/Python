def retailbilling():
    item_name = input("Enter the item name: ")
    quantity = int(input("Enter the quantity: "))
    price_per_item = float(input("Enter the price per item: "))

    total_bill = quantity * price_per_item

    print("\nBILL :-")
    print("Item:", item_name)
    print("Quantity:", quantity)
    print("Price per Item:", round(price_per_item, 2))
    print("Total Bill:", round(total_bill, 2))

retailbilling()