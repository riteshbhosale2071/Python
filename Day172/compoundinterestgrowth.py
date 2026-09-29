def compoundinterestgrowth():
    print("Compound Interest Growth Table :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    print("\nYear\tInterest\tTotal Amount")

    for year in range(1, years + 1):
        amount = principal * (1 + rate / 100) ** year
        interest = amount - principal

        print(year, "\t", round(interest, 2), "\t\t", round(amount, 2))

compoundinterestgrowth()