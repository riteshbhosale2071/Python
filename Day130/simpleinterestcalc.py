def simpleinterestcalc():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time (in years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Please enter non-negative values.")
        return

    interest = (principal * rate * time) / 100
    amount = principal + interest

    print("Simple Interest:", interest)
    print("Total Amount:", amount)

simpleinterestcalc()