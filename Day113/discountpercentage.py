def discountpercentage():
    original_price = float(input("Enter the original price: "))
    selling_price = float(input("Enter the selling price: "))

    discount = original_price - selling_price
    discount_percentage = (discount / original_price) * 100

    print("Discount Amount:", discount)
    print("Discount Percentage:", round(discount_percentage, 2), "%")

discountpercentage()