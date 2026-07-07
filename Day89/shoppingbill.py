def shoppingbill():
    item1 = float(input("Enter price of item 1: "))
    item2 = float(input("Enter price of item 2: "))
    item3 = float(input("Enter price of item 3: "))

    total = item1 + item2 + item3

    print("Total Bill:", total)

    if total >= 1000:
        print("Expensive Shopping")
    else:
        print("Budget Shopping")

shoppingbill()