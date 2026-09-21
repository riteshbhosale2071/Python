def markedpricerecovery():
    print("Marked Price Recovery Program :")

    selling_price = float(input("Enter the selling price: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    if selling_price > 0 and 0 <= discount_percentage < 100:
        marked_price = selling_price / (1 - discount_percentage / 100)
        discount_amount = marked_price - selling_price

        print("Recovered Marked Price:", round(marked_price, 2))
        print("Discount Amount:", round(discount_amount, 2))
        print("Selling Price:", round(selling_price, 2))
    else:
        print("Enter a valid selling price and discount percentage.")

markedpricerecovery()