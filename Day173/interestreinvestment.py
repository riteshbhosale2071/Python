def interestreinvestment():
    print("Interest Reinvestment Simulator :")

    principal = float(input("Enter initial principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    balance = principal
    total_interest = 0

    print("\nYear\tInterest\tReinvested\tBalance")

    for year in range(1, years + 1):
        interest = balance * rate / 100
        balance = balance + interest
        total_interest = total_interest + interest

        print(year, "\t", round(interest, 2), "\t\t", round(interest, 2), "\t\t", round(balance, 2))

    print("\nFinal Result :")
    print("Initial Principal:", round(principal, 2))
    print("Total Reinvested Interest:", round(total_interest, 2))
    print("Final Balance:", round(balance, 2))

interestreinvestment()