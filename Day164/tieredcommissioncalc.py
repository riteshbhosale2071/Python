def tieredcommissioncalc():
    print("Tiered Commission Calculator :")

    sales_amount = float(input("Enter the total sales amount: "))

    if sales_amount >= 0:
        if sales_amount <= 10000:
            commission_rate = 5
        elif sales_amount <= 25000:
            commission_rate = 8
        elif sales_amount <= 50000:
            commission_rate = 10
        else:
            commission_rate = 12

        commission = sales_amount * commission_rate / 100
        total_income = sales_amount + commission

        print("Sales Amount:", round(sales_amount, 2))
        print("Commission Rate:", commission_rate, "%")
        print("Commission Amount:", round(commission, 2))
        print("Total Income:", round(total_income, 2))
    else:
        print("Sales amount cannot be negative.")

tieredcommissioncalc()