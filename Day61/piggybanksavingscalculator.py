def savings():
    days = int(input("Enter number of days: "))
    
    daily_saving = float(input("Enter daily saving amount: ₹"))

    total = days * daily_saving

    print("Total Savings = ₹", total)

savings()