def investmentbreakevenfinder():
    print("Investment Break-Even Finder :")

    investment = float(input("Enter initial investment: "))
    annual_return = float(input("Enter annual return amount: "))

    if investment <= 0 or annual_return <= 0:
        print("Enter valid values.")
        return

    years = 0
    total_return = 0

    while total_return < investment:
        total_return += annual_return
        years += 1

    print("\nBreak-Even Result :")
    print("Initial Investment:", round(investment, 2))
    print("Annual Return:", round(annual_return, 2))
    print("Break-Even Time:", years, "years")
    print("Total Return at Break-Even:", round(total_return, 2))

investmentbreakevenfinder()