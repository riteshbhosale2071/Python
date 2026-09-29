def compoundinteresttargetfinder():
    print("Compound Interest Target Finder :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    target = float(input("Enter target amount: "))

    if principal <= 0 or rate <= 0 or target <= principal:
        print("Enter valid values. Target must be greater than principal.")
        return

    amount = principal
    years = 0

    while amount < target:
        interest = amount * rate / 100
        amount = amount + interest
        years += 1

    print("\nInitial Principal:", round(principal, 2))
    print("Annual Interest Rate:", rate, "%")
    print("Target Amount:", round(target, 2))
    print("Years Required:", years)
    print("Amount Reached:", round(amount, 2))
    print("Interest Earned:", round(amount - principal, 2))

compoundinteresttargetfinder()