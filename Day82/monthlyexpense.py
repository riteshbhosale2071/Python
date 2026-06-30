def expense():
    n = int(input("Enter number of expenses: "))

    expenses = []

    for i in range(n):
        amount = float(input(f"Enter expense {i+1}: "))
        expenses.append(amount)

    print("\nMonthly Expense Report")
    print("-" * 30)

    print("Expenses:", expenses)
    print("Highest Expense =", max(expenses))
    print("Lowest Expense =", min(expenses))
    print("Total Expense =", sum(expenses))
    print("Average Expense =", round(sum(expenses) / n, 2))

expense()