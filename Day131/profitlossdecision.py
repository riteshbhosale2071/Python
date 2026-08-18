def profitlossdecision():
    cost_price = float(input("Enter cost price: "))
    selling_price = float(input("Enter selling price: "))

    if cost_price <= 0 or selling_price < 0:
        print("Please enter valid values.")
        return

    if selling_price > cost_price:
        profit = selling_price - cost_price
        percentage = (profit / cost_price) * 100

        print("Result: Profit")
        print("Profit Amount:", profit)
        print("Profit Percentage:", percentage, "%")

    elif selling_price < cost_price:
        loss = cost_price - selling_price
        percentage = (loss / cost_price) * 100

        print("Result: Loss")
        print("Loss Amount:", loss)
        print("Loss Percentage:", percentage, "%")

    else:
        print("Result: No Profit, No Loss.")

profitlossdecision()