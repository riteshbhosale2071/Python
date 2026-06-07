def expense():
    days = int(input("Enter number of days: "))

    total = 0

    for i in range(days):
        expense = float(input(f"Enter expense for day {i+1}: "))
        total += expense

    print("Total Expense = ₹", total)

expense()