def marketprice():
    price1 = float(input("Enter the price in Market 1: "))
    price2 = float(input("Enter the price in Market 2: "))

    print("Market 1 Price:", price1)
    print("Market 2 Price:", price2)

    if price1 < price2:
        print("Market 1 offers the lower price.")
        print("Difference:", round(price2 - price1, 2))
    elif price2 < price1:
        print("Market 2 offers the lower price.")
        print("Difference:", round(price1 - price2, 2))
    else:
        print("Both markets have the same price.")

marketprice()