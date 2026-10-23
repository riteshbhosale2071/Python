def monthlybudgetallocator():
    print("Monthly Budget Allocator :")

    try:
        monthly_income = float(input("Enter your monthly income: "))
        n = int(input("Enter the number of expense categories: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if monthly_income < 0:
        print("Monthly income cannot be negative.")
        return

    if n <= 0:
        print("Number of categories must be greater than zero.")
        return

    categories = []
    budgets = []

    print("\nEnter your expense categories and planned budgets.")

    for i in range(n):
        category = input("\nEnter category name: ")

        try:
            amount = float(input("Enter budget for " + category + ": "))
        except ValueError:
            print("Invalid budget amount!")
            return

        if amount < 0:
            print("Budget cannot be negative.")
            return

        categories.append(category)
        budgets.append(amount)

    total_budget = sum(budgets)
    remaining_balance = monthly_income - total_budget

    print("\nMonthly Budget Allocation :")
    print("Monthly Income:", round(monthly_income, 2))
    print("-" * 45)
    print("{:<20}{:<15}{:<10}".format("Category", "Budget", "Percent"))

    for i in range(n):
        if monthly_income > 0:
            percentage = (budgets[i] / monthly_income) * 100
        else:
            percentage = 0

        print(
            "{:<20}{:<15.2f}{:<10.2f}".format(
                categories[i], budgets[i], percentage
            )
        )

    print("-" * 45)
    print("Total Allocated Budget:", round(total_budget, 2))
    print("Remaining Balance:", round(remaining_balance, 2))

    print("\nBudget Analysis :")

    if total_budget > monthly_income:
        print("Warning: Your budget exceeds your monthly income.")
        print("Amount Over Budget:", round(total_budget - monthly_income, 2))
    elif total_budget == monthly_income:
        print("Your entire monthly income has been allocated.")
    else:
        print("Your budget is within your monthly income.")
        print("Unallocated Income:", round(remaining_balance, 2))

    if total_budget > 0:
        largest_index = budgets.index(max(budgets))
        smallest_index = budgets.index(min(budgets))

        print("\nLargest Allocation:", categories[largest_index])
        print("Amount:", round(budgets[largest_index], 2))

        print("Smallest Allocation:", categories[smallest_index])
        print("Amount:", round(budgets[smallest_index], 2))

    print("\nAllocation Verification :")
    print("Sum of Category Budgets:", round(sum(budgets), 2))

    if abs(sum(budgets) - total_budget) < 0.01:
        print("Verification successful: All allocations are accounted for.")
    else:
        print("A difference was detected in the allocation totals.")

monthlybudgetallocator()