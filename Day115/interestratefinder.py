def interestratefinder():
    principal = float(input("Enter the principal amount: "))
    simple_interest = float(input("Enter the simple interest: "))
    time = float(input("Enter the time (in years): "))

    rate = (simple_interest * 100) / (principal * time)

    print("Interest Rate:", round(rate, 2), "%")

interestratefinder()