def commissionrate():
    print("Commission Rate Finder :")

    sales_amount = float(input("Enter the total sales amount: "))
    commission_amount = float(input("Enter the commission amount: "))

    if sales_amount > 0 and commission_amount >= 0:
        commission_rate = (commission_amount / sales_amount) * 100

        print("Commission Rate:", round(commission_rate, 2), "%")
    else:
        print("Enter valid sales and commission amounts.")

commissionrate()