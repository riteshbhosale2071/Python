def taxpercentage():
    amount = float(input("Enter the original amount: "))
    tax_rate = float(input("Enter the tax percentage: "))

    tax = (amount * tax_rate) / 100
    total_amount = amount + tax

    print("Tax Amount:", round(tax, 2))
    print("Total Amount:", round(total_amount, 2))

taxpercentage()