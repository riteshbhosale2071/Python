def investmentmilestone():
    print("Investment Milestone :")

    principal = float(input("Enter initial investment: "))
    rate = float(input("Enter annual growth rate (%): "))
    target = float(input("Enter target amount: "))

    if principal <= 0 or rate <= 0 or target <= principal:
        print("Enter valid values.")
        return

    amount = principal
    year = 0

    while amount < target:
        amount = amount * (1 + rate / 100)
        year += 1

    print("\nMilestone Result :")
    print("Initial Investment:", round(principal, 2))
    print("Target Amount:", round(target, 2))
    print("Years Required:", year)
    print("Amount Reached:", round(amount, 2))

investmentmilestone()