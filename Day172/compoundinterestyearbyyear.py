def compoundinterestyearbyyear():
    print("Compound Interest Year-by-Year Simulator :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    balance = principal

    print("\nYear\tInterest\tBalance")

    for year in range(1, years + 1):
        interest = balance * rate / 100
        balance = balance + interest

        print(year, "\t", round(interest, 2), "\t\t", round(balance, 2))

    total_interest = balance - principal

    print("\nInitial Principal:", round(principal, 2))
    print("Total Interest Earned:", round(total_interest, 2))
    print("Final Balance:", round(balance, 2))

compoundinterestyearbyyear()