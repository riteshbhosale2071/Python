def financialgoalpriority():
    print("Financial Goal Priority :")

    try:
        n = int(input("Enter the number of financial goals: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if n <= 0:
        print("Number of goals must be greater than zero.")
        return

    goals = []

    for i in range(n):
        print("\nEnter details for Goal", i + 1)
        name = input("Enter goal name: ")

        try:
            target_amount = float(input("Enter target amount: "))
            current_savings = float(input("Enter current savings for this goal: "))
            months = int(input("Enter desired completion time in months: "))
            importance = int(input("Enter importance level (1-5): "))
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")
            return

        if target_amount < 0 or current_savings < 0:
            print("Amounts cannot be negative.")
            return

        if months <= 0:
            print("Completion time must be greater than zero.")
            return

        if importance < 1 or importance > 5:
            print("Importance level must be between 1 and 5.")
            return

        remaining_amount = max(0, target_amount - current_savings)
        monthly_saving = remaining_amount / months

        urgency = 1 / months
        priority_score = importance * 0.6 + urgency * 100 * 0.4

        goals.append({
            "name": name,
            "target": target_amount,
            "saved": current_savings,
            "remaining": remaining_amount,
            "months": months,
            "importance": importance,
            "monthly_saving": monthly_saving,
            "priority": priority_score
        })

    try:
        available_monthly_savings = float(
            input("\nEnter the total amount available for monthly savings: ")
        )
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    if available_monthly_savings < 0:
        print("Available monthly savings cannot be negative.")
        return

    goals.sort(key=lambda goal: goal["priority"], reverse=True)

    print("\nFinancial Goal Priority Ranking :")

    for rank, goal in enumerate(goals, start=1):
        print("\nPriority Rank:", rank)
        print("Goal:", goal["name"])
        print("Target Amount:", round(goal["target"], 2))
        print("Current Savings:", round(goal["saved"], 2))
        print("Remaining Amount:", round(goal["remaining"], 2))
        print("Importance Level:", goal["importance"], "/ 5")
        print("Desired Completion:", goal["months"], "months")
        print("Required Monthly Savings:", round(goal["monthly_saving"], 2))
        print("Priority Score:", round(goal["priority"], 2))

    print("\nMonthly Savings Allocation :")

    remaining_budget = available_monthly_savings
    total_allocated = 0

    for goal in goals:
        required = goal["monthly_saving"]
        allocation = min(required, remaining_budget)

        remaining_budget -= allocation
        total_allocated += allocation

        print("\nGoal:", goal["name"])
        print("Required Monthly Amount:", round(required, 2))
        print("Allocated Monthly Amount:", round(allocation, 2))

        if allocation >= required:
            print("Status: Monthly target can be met.")
        else:
            print("Status: Monthly target cannot be fully met.")

    print("\nFinal Summary :")
    print("Total Available Monthly Savings:",
          round(available_monthly_savings, 2))
    print("Total Monthly Amount Allocated:", round(total_allocated, 2))
    print("Unallocated Monthly Savings:", round(remaining_budget, 2))

    if remaining_budget == 0:
        print("All available monthly savings have been allocated.")
    else:
        print("Some monthly savings remain available.")

    print("\nNote: Priority scores are based on importance and urgency.")
    print("Review your priorities before making financial decisions.")

financialgoalpriority()