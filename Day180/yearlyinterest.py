def yearlyinterest():
    print("Yearly Interest Tracker :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    total_interest = 0
    current_amount = principal

    for year in range(1, years + 1):
        interest = current_amount * rate / 100
        current_amount += interest
        total_interest += interest

        print("\nYear", year)
        print("Interest:", round(interest, 2))
        print("Amount:", round(current_amount, 2))

    print("\nInterest Summary :")
    print("Principal Amount:", round(principal, 2))
    print("Total Interest:", round(total_interest, 2))
    print("Final Amount:", round(current_amount, 2))

yearlyinterest()