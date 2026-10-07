def compoundinterestgrowthpercent():
    print("Compound Interest Growth Percent :")

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or rate < 0 or years <= 0:
        print("Enter valid values.")
        return

    final_amount = principal * (1 + rate / 100) ** years
    growth_amount = final_amount - principal
    growth_percentage = (growth_amount / principal) * 100

    print("\nGrowth Result :")
    print("Principal Amount:", round(principal, 2))
    print("Final Amount:", round(final_amount, 2))
    print("Growth Amount:", round(growth_amount, 2))
    print("Growth Percentage:", round(growth_percentage, 2), "%")

compoundinterestgrowthpercent()