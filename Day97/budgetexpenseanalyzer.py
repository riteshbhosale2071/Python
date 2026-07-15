def budgetexpense():
    budget = float(input("Enter total budget: "))
    expense1 = float(input("Enter first expense: "))
    expense2 = float(input("Enter second expense: "))

    total_expense = expense1 + expense2
    remaining = budget - total_expense

    print("Total Expense:", total_expense)
    print("Remaining Budget:", remaining)

budgetexpense()