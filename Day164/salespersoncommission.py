def salespersoncommission():
    print("Salesperson Commission Tracker :")

    total_sales = 0
    total_commission = 0

    number_of_sales = int(input("Enter the number of sales: "))

    if number_of_sales > 0:
        for i in range(1, number_of_sales + 1):
            sales_amount = float(input("Enter sales amount for sale " + str(i) + ": "))
            commission_rate = float(input("Enter commission rate for sale " + str(i) + ": "))

            if sales_amount >= 0 and commission_rate >= 0:
                commission = sales_amount * commission_rate / 100

                total_sales += sales_amount
                total_commission += commission

                print("Commission for sale", i, ":", round(commission, 2))
            else:
                print("Invalid sales amount or commission rate.")

        print("\nTotal Sales:", round(total_sales, 2))
        print("Total Commission:", round(total_commission, 2))

        if total_sales > 0:
            average_commission_rate = (total_commission / total_sales) * 100
            print("Average Commission Rate:", round(average_commission_rate, 2), "%")
    else:
        print("Number of sales must be greater than zero.")

salespersoncommission()