def piggybank():
    days = int(input("Enter number of days: "))

    total_savings = 0

    for i in range(days):
        amount = float(input(f"Enter savings for day {i+1}: ₹"))
        total_savings += amount

    print("Total Savings = ₹", total_savings)

piggybank()