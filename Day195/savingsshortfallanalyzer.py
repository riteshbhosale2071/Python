def savingsshortfallanalyzer():
    print("Savings Shortfall Analyzer :")

    try:
        savings_goal = float(input("Enter your savings goal: "))
        current_savings = float(input("Enter your current savings: "))
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your monthly expenses: "))
        target_months = int(input("Enter the number of months to reach the goal: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if savings_goal < 0 or current_savings < 0:
        print("Savings amounts cannot be negative.")
        return

    if monthly_income < 0 or monthly_expenses < 0:
        print("Income and expenses cannot be negative.")
        return

    if target_months <= 0:
        print("Target months must be greater than zero.")
        return

    remaining_goal = max(0, savings_goal - current_savings)
    monthly_savings_needed = remaining_goal / target_months
    available_monthly_savings = monthly_income - monthly_expenses
    total_possible_savings = current_savings + (
        max(0, available_monthly_savings) * target_months
    )

    print("\nSavings Analysis :")
    print("Savings Goal:", round(savings_goal, 2))
    print("Current Savings:", round(current_savings, 2))
    print("Remaining Goal:", round(remaining_goal, 2))
    print("Monthly Income:", round(monthly_income, 2))
    print("Monthly Expenses:", round(monthly_expenses, 2))
    print("Available Monthly Savings:", round(available_monthly_savings, 2))
    print("Target Duration:", target_months, "months")

    print("\nShortfall Calculation :")
    print("Required Monthly Savings:", round(monthly_savings_needed, 2))

    if available_monthly_savings >= 0:
        shortfall = max(0, remaining_goal - (
            available_monthly_savings * target_months
        ))
        print("Projected Savings:", round(total_possible_savings, 2))
        print("Savings Shortfall:", round(shortfall, 2))

        if remaining_goal == 0:
            print("Status: Your savings goal has already been reached.")
        elif shortfall == 0:
            print("Status: You can reach your goal within the target period.")
        else:
            print("Status: Your projected savings fall short of your goal.")
            print("Additional Monthly Savings Needed:",
                  round(shortfall / target_months, 2))
    else:
        print("Status: Your expenses exceed your monthly income.")
        print("Monthly Deficit:", round(abs(available_monthly_savings), 2))
        print("Reduce expenses or increase income before planning additional savings.")

    print("\nGoal Progress :")

    if savings_goal > 0:
        progress = min(100, current_savings / savings_goal * 100)
        print("Savings Progress:", round(progress, 2), "%")
    else:
        print("Savings Progress: 100.00%")

    if remaining_goal > 0 and available_monthly_savings > 0:
        months_needed = remaining_goal / available_monthly_savings
        whole_months = int(months_needed)

        if months_needed > whole_months:
            whole_months += 1

        print("Estimated Months to Reach Goal:", whole_months)
    elif remaining_goal == 0:
        print("Estimated Months to Reach Goal: 0")
    else:
        print("Estimated completion time cannot be calculated with current savings.")

    print("\nFinal Summary :")
    print("Savings Goal:", round(savings_goal, 2))
    print("Current Savings:", round(current_savings, 2))
    print("Amount Needed:", round(remaining_goal, 2))
    print("Target Completion:", target_months, "months")

savingsshortfallanalyzer()