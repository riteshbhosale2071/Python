def investmentgrowthcomparison():
    print("Investment 1")
    principal1 = float(input("Enter principal amount: "))
    rate1 = float(input("Enter annual interest rate (%): "))
    time1 = float(input("Enter time (years): "))

    print("\nInvestment 2")
    principal2 = float(input("Enter principal amount: "))
    rate2 = float(input("Enter annual interest rate (%): "))
    time2 = float(input("Enter time (years): "))

    if (principal1 <= 0 or rate1 < 0 or time1 < 0 or
            principal2 <= 0 or rate2 < 0 or time2 < 0):
        print("Enter valid investment details.")
        return

    # Simple interest growth
    interest1 = (principal1 * rate1 * time1) / 100
    interest2 = (principal2 * rate2 * time2) / 100

    amount1 = principal1 + interest1
    amount2 = principal2 + interest2

    print("\n--- Investment Growth Comparison ---")
    print("Investment 1 Final Amount:", amount1)
    print("Investment 2 Final Amount:", amount2)

    if amount1 > amount2:
        print("Investment 1 has higher growth.")
    elif amount2 > amount1:
        print("Investment 2 has higher growth.")
    else:
        print("Both investments have the same growth.")

investmentgrowthcomparison()