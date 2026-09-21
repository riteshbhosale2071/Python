def successivediscountcalc():
    print("Successive Discount Calculator :")

    marked_price = float(input("Enter the marked price: "))
    discount1 = float(input("Enter the first discount percentage: "))
    discount2 = float(input("Enter the second discount percentage: "))

    if marked_price > 0 and 0 <= discount1 <= 100 and 0 <= discount2 <= 100:
        price_after_first = marked_price - (marked_price * discount1 / 100)
        final_price = price_after_first - (price_after_first * discount2 / 100)

        total_discount = marked_price - final_price
        effective_discount = (total_discount / marked_price) * 100

        print("Price after first discount:", round(price_after_first, 2))
        print("Final price:", round(final_price, 2))
        print("Total discount amount:", round(total_discount, 2))
        print("Effective discount percentage:", round(effective_discount, 2), "%")
    else:
        print("Enter valid price and discount percentages.")

successivediscountcalc()