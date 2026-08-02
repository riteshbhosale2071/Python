def principalfinder():
    simple_interest = float(input("Enter the simple interest: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time (in years): "))

    principal = (simple_interest * 100) / (rate * time)

    print("Principal Amount:", round(principal, 2))

principalfinder()