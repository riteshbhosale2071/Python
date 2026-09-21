def commissioncomparison():
    print("Commission Comparison Program :")

    sales1 = float(input("Enter sales amount for salesperson 1: "))
    rate1 = float(input("Enter commission rate for salesperson 1: "))

    sales2 = float(input("Enter sales amount for salesperson 2: "))
    rate2 = float(input("Enter commission rate for salesperson 2: "))

    if sales1 > 0 and sales2 > 0 and rate1 >= 0 and rate2 >= 0:
        commission1 = sales1 * rate1 / 100
        commission2 = sales2 * rate2 / 100

        print("Commission of salesperson 1:", round(commission1, 2))
        print("Commission of salesperson 2:", round(commission2, 2))

        if commission1 > commission2:
            print("Salesperson 1 earns more commission.")
            print("Difference:", round(commission1 - commission2, 2))
        elif commission2 > commission1:
            print("Salesperson 2 earns more commission.")
            print("Difference:", round(commission2 - commission1, 2))
        else:
            print("Both salespersons earn the same commission.")
    else:
        print("Enter valid sales amounts and commission rates.")

commissioncomparison()