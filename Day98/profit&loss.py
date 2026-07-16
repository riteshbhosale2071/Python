def profit_loss():
    cost_price = float(input("Enter Cost Price: "))
    selling_price = float(input("Enter Selling Price: "))
    
    difference = selling_price - cost_price

    if difference > 0:
        print("Profit =", difference)
    elif difference < 0:
        print("Loss =", abs(difference))
    else:
        print("No Profit No Loss")

profit_loss()