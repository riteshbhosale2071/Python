def recharge():
    plan_price = float(input("Enter recharge plan amount: ₹"))
    
    tax = float(input("Enter tax amount: ₹"))

    total = plan_price + tax

    print("Total Recharge Cost = ₹", total)

recharge()