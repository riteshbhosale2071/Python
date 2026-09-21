def bestshoppingdeal():
    print("Best Shopping Deal Finder :")

    marked_price = float(input("Enter the marked price: "))

    discount1 = float(input("Enter discount percentage for offer 1: "))
    discount2 = float(input("Enter first discount percentage for offer 2: "))
    discount3 = float(input("Enter second discount percentage for offer 2: "))

    if marked_price > 0 and 0 <= discount1 <= 100 and 0 <= discount2 <= 100 and 0 <= discount3 <= 100:
        price1 = marked_price - (marked_price * discount1 / 100)

        price_after_discount2 = marked_price - (marked_price * discount2 / 100)
        price2 = price_after_discount2 - (price_after_discount2 * discount3 / 100)

        discount_amount1 = marked_price - price1
        discount_amount2 = marked_price - price2

        print("\nOffer 1 Final Price:", round(price1, 2))
        print("Offer 1 Savings:", round(discount_amount1, 2))

        print("\nOffer 2 Final Price:", round(price2, 2))
        print("Offer 2 Savings:", round(discount_amount2, 2))

        if price1 < price2:
            print("\nBest Deal: Offer 1")
            print("Extra Savings:", round(price2 - price1, 2))
        elif price2 < price1:
            print("\nBest Deal: Offer 2")
            print("Extra Savings:", round(price1 - price2, 2))
        else:
            print("\nBoth offers provide the same final price.")

    else:
        print("Enter valid price and discount percentages.")

bestshoppingdeal()