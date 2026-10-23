def emergencyfundestimator():
    print("Emergency Fund Estimator :")

    try:
        monthly_expenses = float(input("Enter your monthly essential expenses: "))
        current_savings = float(input("Enter your current emergency savings: "))
        target_months = int(input("Enter the number of months to cover (3, 6, or 12): "))
        monthly_contribution = float(input("Enter your planned monthly savings: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if monthly_expenses < 0 or current_savings < 0 or monthly_contribution < 0:
        print("Expenses, savings, and contributions cannot be negative.")
        return

    if target_months <= 0:
        print("Target months must be greater than zero.")
        return

    target_fund = monthly_expenses * target_months
    remaining_amount = max(0, target_fund - current_savings)

    print("\nEmergency Fund Summary :")
    print("Monthly Essential Expenses:", round(monthly_expenses, 2))
    print("Current Emergency Savings:", round(current_savings, 2))
    print("Target Coverage:", target_months, "months")
    print("Target Emergency Fund:", round(target_fund, 2))
    print("Amount Still Required:", round(remaining_amount, 2))

    if target_fund > 0:
        progress = min(100, (current_savings / target_fund) * 100)
    else:
        progress = 100

    print("Fund Completion:", round(progress, 2), "%")

    print("\nSavings Plan :")

    if remaining_amount == 0:
        print("Congratulations! Your emergency fund target is reached.")
        print("Amount Above Target:", round(max(0, current_savings - target_fund), 2))
    elif monthly_contribution > 0:
        months_needed = remaining_amount / monthly_contribution
        whole_months = int(months_needed)

        if months_needed > whole_months:
            whole_months += 1

        print("Planned Monthly Contribution:", round(monthly_contribution, 2))
        print("Estimated Months to Reach Goal:", whole_months)
        print("Estimated Additional Savings:", round(
            whole_months * monthly_contribution, 2
        ))

        years = whole_months // 12
        months = whole_months % 12

        if years > 0:
            print("Estimated Time:", years, "years and", months, "months")
        else:
            print("Estimated Time:", months, "months")
    else:
        print("Monthly contribution is zero.")
        print("Start saving regularly to reach your emergency fund target.")

    print("\nCoverage Analysis :")

    if monthly_expenses > 0:
        coverage = current_savings / monthly_expenses
        print("Current Expense Coverage:", round(coverage, 2), "months")

        if coverage < 3:
            print("Status: Build your emergency savings toward at least 3 months.")
        elif coverage < 6:
            print("Status: You have a basic reserve; consider building toward 6 months.")
        else:
            print("Status: Your savings cover at least 6 months of essential expenses.")
    else:
        print("Monthly expenses are zero, so expense coverage cannot be calculated.")

    print("\nNote: This estimate excludes interest, inflation, and unexpected changes.")
    print("Choose a target based on your income stability and personal needs.")

emergencyfundestimator()