def timeperiodcalc():
    principal = float(input("Enter the principal amount: "))
    simple_interest = float(input("Enter the simple interest: "))
    rate = float(input("Enter the annual interest rate (%): "))

    time = (simple_interest * 100) / (principal * rate)

    print("Time Period:", round(time, 2), "years")

timeperiodcalc()