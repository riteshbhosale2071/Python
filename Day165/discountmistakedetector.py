def discountmistakedetector():
    print("Discount Mistake Detector :")

    marked_price = float(input("Enter the marked price: "))
    discount_percentage = float(input("Enter the stated discount percentage: "))
    final_price = float(input("Enter the actual final price: "))

    if marked_price > 0 and 0 <= discount_percentage <= 100 and final_price >= 0:
        expected_discount = marked_price * discount_percentage / 100
        expected_price = marked_price - expected_discount

        actual_discount = marked_price - final_price
        actual_discount_percentage = (actual_discount / marked_price) * 100

        print("Expected Discount Amount:", round(expected_discount, 2))
        print("Expected Final Price:", round(expected_price, 2))
        print("Actual Discount Amount:", round(actual_discount, 2))
        print("Actual Discount Percentage:", round(actual_discount_percentage, 2), "%")

        if final_price == expected_price:
            print("No discount mistake detected.")
        elif final_price < expected_price:
            print("Mistake detected: An additional discount was applied.")
            print("Extra Discount:", round(expected_price - final_price, 2))
        else:
            print("Mistake detected: The applied discount is lower than stated.")
            print("Extra Amount Charged:", round(final_price - expected_price, 2))
    else:
        print("Enter valid price, discount, and final price values.")

discountmistakedetector()