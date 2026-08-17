def partnershipprofitcalc():
    total_profit = float(input("Enter total profit: "))

    investment1 = float(input("Enter Partner 1 investment: "))
    time1 = float(input("Enter Partner 1 investment time: "))

    investment2 = float(input("Enter Partner 2 investment: "))
    time2 = float(input("Enter Partner 2 investment time: "))

    if total_profit < 0 or investment1 <= 0 or investment2 <= 0 or time1 <= 0 or time2 <= 0:
        print("Please enter valid positive values.")
        return

    share1 = investment1 * time1
    share2 = investment2 * time2

    total_share = share1 + share2

    profit1 = (share1 / total_share) * total_profit
    profit2 = (share2 / total_share) * total_profit

    print("Partner 1 Profit:", profit1)
    print("Partner 2 Profit:", profit2)

partnershipprofitcalc()