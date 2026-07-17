def vehiclepurchase():
    vehicle_price = float(input("Enter vehicle price: "))
    tax = float(input("Enter tax amount: "))
    insurance = float(input("Enter insurance amount: "))

    total_cost = vehicle_price + tax + insurance

    print("Total Vehicle Purchase Cost =", total_cost)

vehiclepurchase()