def totalamount():
    principal = float(input("Enter the principal amount: "))
    interest = float(input("Enter the interest amount: "))

    total_amount = principal + interest

    print("Principal Amount:", principal)
    print("Interest Amount:", interest)
    print("Total Amount:", round(total_amount, 2))

totalamount()