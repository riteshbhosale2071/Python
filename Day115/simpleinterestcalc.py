def simpleinterest():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time (in years): "))

    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest

    print("Simple Interest:", round(simple_interest, 2))
    print("Total Amount:", round(total_amount, 2))

simpleinterest()