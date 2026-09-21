def effectivediscountpercentage():
    print("Effective Discount Percentage :")

    discount1 = float(input("Enter the first discount percentage: "))
    discount2 = float(input("Enter the second discount percentage: "))

    if 0 <= discount1 <= 100 and 0 <= discount2 <= 100:
        effective_discount = discount1 + discount2 - (discount1 * discount2 / 100)

        print("Effective Discount Percentage:", round(effective_discount, 2), "%")
    else:
        print("Discount percentages must be between 0 and 100.")

effectivediscountpercentage()