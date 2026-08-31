def simpleinterestcomparison():
    print("Enter details for Investment 1:")
    principal1 = float(input("Enter principal amount: "))
    rate1 = float(input("Enter interest rate (%): "))
    time1 = float(input("Enter time (years): "))

    print("\nEnter details for Investment 2:")
    principal2 = float(input("Enter principal amount: "))
    rate2 = float(input("Enter interest rate (%): "))
    time2 = float(input("Enter time (years): "))

    if (principal1 <= 0 or rate1 < 0 or time1 < 0 or
            principal2 <= 0 or rate2 < 0 or time2 < 0):
        print("Enter valid values.")
        return

    interest1 = (principal1 * rate1 * time1) / 100
    interest2 = (principal2 * rate2 * time2) / 100

    amount1 = principal1 + interest1
    amount2 = principal2 + interest2

    print("\n--- Simple Interest Comparison ---")
    print("Investment 1 Interest:", interest1)
    print("Investment 1 Amount:", amount1)

    print("Investment 2 Interest:", interest2)
    print("Investment 2 Amount:", amount2)

    if interest1 > interest2:
        print("Investment 1 earns more interest.")
    elif interest2 > interest1:
        print("Investment 2 earns more interest.")
    else:
        print("Both investments earn the same interest.")

simpleinterestcomparison()