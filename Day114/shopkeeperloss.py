def shopkeeperloss():
    cost_price = float(input("Enter the cost price: "))
    selling_price = float(input("Enter the selling price: "))

    loss = cost_price - selling_price

    if loss > 0:
        loss_percentage = (loss / cost_price) * 100
        print("Loss:", loss)
        print("Loss Percentage:", round(loss_percentage, 2), "%")
    elif loss < 0:
        print("Profit:", abs(loss))
    else:
        print("No Profit, No Loss")

shopkeeperloss()