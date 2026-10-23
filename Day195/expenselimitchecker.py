def expenselimitchecker():
    print("Expense Limit Checker :")

    try:
        monthly_limit = float(input("Enter your monthly expense limit: "))
        n = int(input("Enter the number of expense categories: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if monthly_limit < 0:
        print("Expense limit cannot be negative.")
        return

    if n <= 0:
        print("Number of categories must be greater than zero.")
        return

    categories = []
    expenses = []
    total_expenses = 0

    for i in range(n):
        print("\nExpense Category", i + 1)
        category = input("Enter category name: ")

        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Invalid expense amount!")
            return

        if amount < 0:
            print("Expense amount cannot be negative.")
            return

        categories.append(category)
        expenses.append(amount)
        total_expenses += amount

    remaining_limit = monthly_limit - total_expenses

    print("\nExpense Report :")
    print("{:<20}{:<15}".format("Category", "Expense"))
    print("-" * 35)

    for i in range(n):
        print("{:<20}{:<15.2f}".format(categories[i], expenses[i]))

    print("-" * 35)
    print("Monthly Expense Limit:", round(monthly_limit, 2))
    print("Total Expenses:", round(total_expenses, 2))
    print("Remaining Limit:", round(remaining_limit, 2))

    print("\nLimit Status :")

    if total_expenses > monthly_limit:
        exceeded_amount = total_expenses - monthly_limit
        print("Status: Expense limit exceeded.")
        print("Excess Spending:", round(exceeded_amount, 2))
    elif total_expenses == monthly_limit:
        print("Status: You have reached your expense limit.")
    else:
        print("Status: Expenses are within the limit.")
        print("Available Spending Balance:", round(remaining_limit, 2))

    print("\nCategory Analysis :")

    if total_expenses > 0:
        largest_index = expenses.index(max(expenses))
        smallest_index = expenses.index(min(expenses))

        print("Highest Expense Category:", categories[largest_index])
        print("Highest Expense:", round(expenses[largest_index], 2))

        print("Lowest Expense Category:", categories[smallest_index])
        print("Lowest Expense:", round(expenses[smallest_index], 2))

        print("\nExpense Percentages:")

        for i in range(n):
            percentage = (expenses[i] / total_expenses) * 100
            print(categories[i] + ":", round(percentage, 2), "%")
    else:
        print("No expenses recorded.")

    print("\nFinal Verification :")
    print("Recorded Categories:", len(categories))
    print("Calculated Total:", round(sum(expenses), 2))

    if abs(sum(expenses) - total_expenses) < 0.01:
        print("Verification successful: All expenses are accounted for.")
    else:
        print("Verification failed: Please check the expense records.")

expenselimitchecker()