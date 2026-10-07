def interestratereversecalc():
    print("Interest Rate Reverse Calculator :")

    principal = float(input("Enter principal amount: "))
    final_amount = float(input("Enter final amount: "))
    years = int(input("Enter number of years: "))

    if principal <= 0 or final_amount <= 0 or years <= 0:
        print("Enter valid values.")
        return

    if final_amount < principal:
        print("Final amount cannot be less than principal.")
        return

    rate = ((final_amount / principal) ** (1 / years) - 1) * 100

    print("\nResult :")
    print("Principal Amount:", round(principal, 2))
    print("Final Amount:", round(final_amount, 2))
    print("Time:", years, "years")
    print("Required Annual Interest Rate:", round(rate, 2), "%")

interestratereversecalc()