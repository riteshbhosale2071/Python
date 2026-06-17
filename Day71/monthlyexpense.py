def expense():
    expenses = []

    months = int(input("Enter number of months: "))

    for i in range(months):
        amount = float(input(f"Enter expense for month {i+1}: ₹"))
        expenses.append(amount)

    print("\nTotal Expense = ₹", sum(expenses))
    print("Highest Expense = ₹", max(expenses))
    print("Lowest Expense = ₹", min(expenses))
    print("Average Expense = ₹", sum(expenses) / len(expenses))

expense()