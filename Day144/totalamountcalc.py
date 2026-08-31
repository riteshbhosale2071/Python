def totalamountcalc():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (%): "))
    time = float(input("Enter the time (years): "))

    if principal <= 0 or rate < 0 or time < 0:
        print("Enter valid values.")
        return

    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print("Simple Interest:", simple_interest)
    print("Total Amount:", total_amount)

totalamountcalc()