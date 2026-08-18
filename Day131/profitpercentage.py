def profitpercentage():
    cost_price = float(input("Enter cost price: "))
    selling_price = float(input("Enter selling price: "))

    if cost_price <= 0 or selling_price < 0:
        print("Please enter valid values.")
        return

    if selling_price > cost_price:
        profit = selling_price - cost_price
        profit_percentage = (profit / cost_price) * 100

        print("Profit:", profit)
        print("Profit Percentage:", profit_percentage, "%")

    elif selling_price == cost_price:
        print("No Profit, No Loss.")

    else:
        loss = cost_price - selling_price
        loss_percentage = (loss / cost_price) * 100

        print("Loss:", loss)
        print("Loss Percentage:", loss_percentage, "%")

profitpercentage()