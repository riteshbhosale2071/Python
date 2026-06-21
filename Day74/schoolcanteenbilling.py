def canteen():
    sandwich = 30
    juice = 20
    cake = 25

    qty_sandwich = int(input("Enter quantity of Sandwich: "))
    qty_juice = int(input("Enter quantity of Juice: "))
    qty_cake = int(input("Enter quantity of Cake: "))

    total = (qty_sandwich * sandwich) + \
            (qty_juice * juice) + \
            (qty_cake * cake)

    print("Total Bill = ₹", total)

canteen()