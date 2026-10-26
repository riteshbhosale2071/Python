def financialgoalfeasibility():
    print("Financial Goal Feasibility Checker :")

    def get_non_negative_number(prompt):
        try:
            value = float(input(prompt))

            if value < 0:
                print("Value cannot be negative.")
                return None

            return value
        except ValueError:
            print("Invalid input! Enter a numeric value.")
            return None

    goal_name = input("Enter your financial goal name: ").strip()

    if not goal_name:
        print("Goal name cannot be empty.")
        return

    goal_amount = get_non_negative_number(
        "Enter the target amount (₹): "
    )
    if goal_amount is None:
        return

    current_savings = get_non_negative_number(
        "Enter your current savings (₹): "
    )
    if current_savings is None:
        return

    monthly_savings = get_non_negative_number(
        "Enter the amount you can save monthly (₹): "
    )
    if monthly_savings is None:
        return

    try:
        months = int(input("Enter the number of months to achieve the goal: "))
    except ValueError:
        print("Invalid input! Enter a whole number.")
        return

    if months <= 0:
        print("The time period must be greater than zero.")
        return

    monthly_expenses = get_non_negative_number(
        "Enter your current monthly expenses (₹): "
    )
    if monthly_expenses is None:
        return

    monthly_income = get_non_negative_number(
        "Enter your monthly income (₹): "
    )
    if monthly_income is None:
        return

    annual_return = get_non_negative_number(
        "Enter expected annual investment return (%), or 0 for no growth: "
    )
    if annual_return is None:
        return

    if annual_return > 100:
        print("Please enter an annual return of 100% or less.")
        return

    remaining_amount = max(0, goal_amount - current_savings)
    planned_savings = monthly_savings * months
    projected_savings = current_savings + planned_savings

    monthly_surplus = monthly_income - monthly_expenses
    required_monthly_savings = remaining_amount / months

    monthly_rate = (1 + annual_return / 100) ** (1 / 12) - 1
    projected_investment_value = current_savings

    for month in range(months):
        projected_investment_value = (
            projected_investment_value * (1 + monthly_rate)
            + monthly_savings
        )

    print("\n" + "=" * 48)
    print("        FINANCIAL GOAL FEASIBILITY REPORT")
    print("=" * 48)

    print("\nGoal Name:", goal_name)
    print("Target Amount: ₹{:.2f}".format(goal_amount))
    print("Current Savings: ₹{:.2f}".format(current_savings))
    print("Remaining Amount: ₹{:.2f}".format(remaining_amount))
    print("Time Available:", months, "months")

    print("\nSavings Projection :")
    print("Monthly Savings Plan: ₹{:.2f}".format(monthly_savings))
    print("Total Planned Contributions: ₹{:.2f}".format(planned_savings))
    print("Projected Savings Without Growth: ₹{:.2f}".format(
        projected_savings
    ))
    print("Estimated Value With Investment Growth: ₹{:.2f}".format(
        projected_investment_value
    ))

    print("\nMonthly Budget Analysis :")
    print("Monthly Income: ₹{:.2f}".format(monthly_income))
    print("Monthly Expenses: ₹{:.2f}".format(monthly_expenses))
    print("Monthly Surplus: ₹{:.2f}".format(monthly_surplus))

    print("\nFeasibility Analysis :")

    if remaining_amount == 0:
        print("Status: Goal already achieved!")
    elif monthly_surplus < 0:
        print("Status: Not feasible with the current budget.")
        print("Your monthly expenses exceed your income.")
    elif monthly_savings > monthly_surplus:
        print("Status: Savings plan exceeds your monthly budget.")
        print("Reduce planned savings to fit your available surplus.")
    elif projected_savings >= goal_amount:
        print("Status: FEASIBLE without investment growth.")
        print("Your savings plan can reach the target on time.")
    elif projected_investment_value >= goal_amount:
        print("Status: Potentially feasible with investment growth.")
        print("Actual returns may vary and are not guaranteed.")
    else:
        print("Status: NOT FEASIBLE with the current savings plan.")
        print("Consider increasing savings or extending the deadline.")

    if remaining_amount > 0:
        print("\nRecommended Savings Plan :")
        print("Required Monthly Savings: ₹{:.2f}".format(
            required_monthly_savings
        ))

        if monthly_surplus >= 0:
            print("Maximum Monthly Surplus: ₹{:.2f}".format(
                monthly_surplus
            ))

            if required_monthly_savings <= monthly_surplus:
                print("The goal fits your budget before considering growth.")
            else:
                print("Required savings exceed your current monthly surplus.")
                print("Additional Monthly Income or Expense Reduction Needed: ₹{:.2f}".format(
                    required_monthly_savings - monthly_surplus
                ))

        if monthly_savings > 0:
            months_needed = max(
                0,
                int((remaining_amount + monthly_savings - 1)
                    // monthly_savings)
            )

            print("Estimated Months Needed Without Growth:", months_needed)
        else:
            print("You need to start saving to make progress toward the goal.")

    print("\nFinal Summary :")

    if current_savings >= goal_amount:
        print("Congratulations! You have already achieved your goal.")
    elif monthly_surplus >= 0 and projected_savings >= goal_amount:
        print("Your financial goal is achievable within the given timeline.")
    else:
        print("Review your budget, savings amount, and target deadline.")

    print("\nNote: Investment growth is hypothetical and excludes fees and taxes.")
    print("This program provides an estimate, not financial advice.")
    print("\nFinancial goal feasibility check completed.")

financialgoalfeasibility()