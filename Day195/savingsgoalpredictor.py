def savingsgoalpredictor():
    print("Savings Goal Predictor :")

    try:
        goal = float(input("Enter your savings goal amount: "))
        current_savings = float(input("Enter your current savings: "))
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your monthly expenses: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    if goal < 0 or current_savings < 0:
        print("Savings goal and current savings cannot be negative.")
        return

    if monthly_income < 0 or monthly_expenses < 0:
        print("Income and expenses cannot be negative.")
        return

    monthly_savings = monthly_income - monthly_expenses

    print("\nSavings Analysis :")
    print("Savings Goal:", round(goal, 2))
    print("Current Savings:", round(current_savings, 2))
    print("Monthly Income:", round(monthly_income, 2))
    print("Monthly Expenses:", round(monthly_expenses, 2))
    print("Potential Monthly Savings:", round(monthly_savings, 2))

    remaining_amount = goal - current_savings

    print("\nGoal Prediction :")

    if current_savings >= goal:
        print("Congratulations! You have already reached your savings goal.")
        print("Amount Above Goal:", round(current_savings - goal, 2))
        return

    print("Amount Remaining:", round(remaining_amount, 2))

    if monthly_savings > 0:
        months_needed = remaining_amount / monthly_savings
        whole_months = int(months_needed)

        if months_needed > whole_months:
            whole_months += 1

        print("Estimated Months Required:", whole_months)
        print("Estimated Savings After", whole_months, "Months:",
              round(current_savings + whole_months * monthly_savings, 2))

        years = whole_months // 12
        months = whole_months % 12

        if years > 0:
            print("Estimated Time:", years, "years and", months, "months")
        else:
            print("Estimated Time:", months, "months")

        print("\n=== Savings Recommendations ===")

        if monthly_savings < remaining_amount:
            print("Continue saving consistently to reach your goal.")

        suggested_savings = remaining_amount / 6

        print("Suggested Monthly Savings for a 6-Month Goal:",
              round(suggested_savings, 2))

        if suggested_savings > monthly_savings:
            print("You may need to reduce expenses or increase your income.")
        else:
            print("Your current savings rate can achieve the goal within 6 months.")

    elif monthly_savings == 0:
        print("You have no monthly surplus available for savings.")
        print("Reduce expenses or increase income to reach your goal.")

    else:
        print("Your expenses exceed your income.")
        print("A positive monthly savings amount is needed to reach your goal.")

    print("\nFinal Summary :")
    print("Savings Progress:",
          round((current_savings / goal) * 100, 2) if goal > 0 else 100,
          "%")
    print("Remaining Amount:", round(remaining_amount, 2))

savingsgoalpredictor()