def discountamountrecovery():
    print("Discount Amount Recovery :")

    marked_price = float(input("Enter the marked price: "))
    selling_price = float(input("Enter the selling price: "))

    if marked_price > 0 and selling_price > 0:
        if selling_price <= marked_price:
            discount_amount = marked_price - selling_price
            discount_percentage = (discount_amount / marked_price) * 100

            print("Discount Amount:", round(discount_amount, 2))
            print("Discount Percentage:", round(discount_percentage, 2), "%")
        else:
            print("Selling price cannot be greater than marked price.")
    else:
        print("Prices must be greater than zero.")

discountamountrecovery()