def monthlysavingsgoal():
    try:
        savings_goal = float(input("Enter your savings goal (₹): "))
        current_savings = float(input("Enter your current savings (₹): "))
        monthly_savings = float(input("Enter monthly savings amount (₹): "))

        if savings_goal <= 0 or current_savings < 0 or monthly_savings <= 0:
            print("Please enter valid savings amounts.")
            return

        remaining_amount = savings_goal - current_savings

        if remaining_amount <= 0:
            print("Congratulations! You have already achieved your savings goal.")
            print("Extra Savings: ₹", round(abs(remaining_amount), 2))
            return

        months_required = -(-remaining_amount // monthly_savings)
        years = int(months_required // 12)
        months = int(months_required % 12)

        total_future_savings = current_savings + months_required * monthly_savings

        print("\nMonthly Savings Goal Report")
        print("Savings Goal: ₹", round(savings_goal, 2))
        print("Current Savings: ₹", round(current_savings, 2))
        print("Monthly Savings: ₹", round(monthly_savings, 2))
        print("Remaining Amount: ₹", round(remaining_amount, 2))
        print("Months Required:", int(months_required))
        print("Estimated Time:", years, "years and", months, "months")
        print("Total Savings After Goal: ₹", round(total_future_savings, 2))

    except ValueError:
        print("Please enter valid numeric values.")

monthlysavingsgoal()