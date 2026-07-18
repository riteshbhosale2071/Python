def profitsharing():
    total_profit = float(input("Enter total profit: "))
    partners = int(input("Enter number of partners: "))

    if partners == 0:
        print("Number of partners cannot be zero.")
        return

    share = total_profit / partners

    print("Profit Share per Partner =", share)

profitsharing()