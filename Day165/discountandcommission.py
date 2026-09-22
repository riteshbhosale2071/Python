def discountandcommission():
    print("Discount-and-Commission Analyzer :")

    marked_price = float(input("Enter the marked price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    commission_rate = float(input("Enter the commission rate: "))

    if marked_price > 0 and 0 <= discount_percentage <= 100 and commission_rate >= 0:
        discount_amount = marked_price * discount_percentage / 100
        selling_price = marked_price - discount_amount
        commission_amount = selling_price * commission_rate / 100
        net_revenue = selling_price - commission_amount

        print("Discount Amount:", round(discount_amount, 2))
        print("Selling Price:", round(selling_price, 2))
        print("Commission Amount:", round(commission_amount, 2))
        print("Net Revenue:", round(net_revenue, 2))

        if net_revenue > 0:
            print("The transaction generates positive net revenue.")
        elif net_revenue == 0:
            print("The transaction generates zero net revenue.")
        else:
            print("The transaction generates negative net revenue.")
    else:
        print("Enter valid price, discount, and commission values.")

discountandcommission()