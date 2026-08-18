def bankamtcalc():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time (in years): "))

    if principal < 0 or rate < 0 or time < 0:
        print("Please enter non-negative values.")
        return

    simple_interest = (principal * rate * time) / 100
    final_amount = principal + simple_interest

    print("Interest Earned:", simple_interest)
    print("Final Bank Amount:", final_amount)

bankamtcalc()