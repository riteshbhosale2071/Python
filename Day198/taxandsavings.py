def taxandsavings():
    print("Tax and Savings :")

    def get_positive_number(prompt):
        try:
            value = float(input(prompt))

            if value < 0:
                print("Value cannot be negative.")
                return None

            return value
        except ValueError:
            print("Invalid input! Enter a numeric value.")
            return None

    annual_income = get_positive_number("Enter annual income (₹): ")
    if annual_income is None:
        return

    annual_expenses = get_positive_number("Enter annual expenses (₹): ")
    if annual_expenses is None:
        return

    tax_rate = get_positive_number("Enter estimated tax rate (%): ")
    if tax_rate is None or tax_rate > 100:
        print("Tax rate must be between 0 and 100.")
        return

    savings_goal = get_positive_number("Enter your annual savings goal (₹): ")
    if savings_goal is None:
        return

    monthly_investment = get_positive_number(
        "Enter planned monthly investment (₹): "
    )
    if monthly_investment is None:
        return

    try:
        investment_return = float(
            input("Enter expected annual investment return (%): ")
        )
    except ValueError:
        print("Invalid investment return.")
        return

    if investment_return < -100:
        print("Investment return cannot be below -100%.")
        return

    tax_amount = annual_income * tax_rate / 100
    income_after_tax = annual_income - tax_amount
    disposable_income = income_after_tax - annual_expenses

    if disposable_income < 0:
        available_savings = 0
        deficit = abs(disposable_income)
    else:
        available_savings = disposable_income
        deficit = 0

    planned_annual_investment = monthly_investment * 12
    remaining_after_investment = disposable_income - planned_annual_investment

    print("\n" + "=" * 45)
    print("         TAX AND SAVINGS REPORT")
    print("=" * 45)

    print("\nAnnual Income: ₹{:.2f}".format(annual_income))
    print("Estimated Tax: ₹{:.2f}".format(tax_amount))
    print("Income After Tax: ₹{:.2f}".format(income_after_tax))
    print("Annual Expenses: ₹{:.2f}".format(annual_expenses))
    print("Disposable Income: ₹{:.2f}".format(disposable_income))

    print("\nSavings Analysis :")
    print("Available Annual Savings: ₹{:.2f}".format(available_savings))
    print("Annual Savings Goal: ₹{:.2f}".format(savings_goal))
    print("Planned Annual Investment: ₹{:.2f}".format(
        planned_annual_investment
    ))

    if disposable_income < 0:
        print("Warning: Expenses exceed income after estimated tax.")
        print("Annual Shortfall: ₹{:.2f}".format(deficit))
    elif planned_annual_investment > disposable_income:
        print("Warning: Planned investments exceed disposable income.")
        print("Investment Budget Shortfall: ₹{:.2f}".format(
            planned_annual_investment - disposable_income
        ))
    else:
        print("Remaining Income After Investment: ₹{:.2f}".format(
            remaining_after_investment
        ))

    if savings_goal == 0:
        print("No savings goal has been set.")
    elif available_savings >= savings_goal:
        print("Savings Goal Status: Achievable based on current estimates.")
        print("Amount Above Goal: ₹{:.2f}".format(
            available_savings - savings_goal
        ))
    else:
        shortfall = savings_goal - available_savings
        print("Savings Goal Status: Goal not yet achievable.")
        print("Annual Savings Shortfall: ₹{:.2f}".format(shortfall))

        if disposable_income > 0:
            print("Additional Monthly Savings Needed: ₹{:.2f}".format(
                shortfall / 12
            ))

    print("\nInvestment Growth :")

    if planned_annual_investment == 0:
        print("No planned investment to simulate.")
    elif investment_return == -100:
        print("At a -100% return, the simulated investment value becomes ₹0.")
    else:
        estimated_value = 0

        for month in range(1, 13):
            estimated_value = (
                estimated_value * (1 + investment_return / 100) ** (1 / 12)
                + monthly_investment
            )

        total_invested = planned_annual_investment
        estimated_gain = estimated_value - total_invested

        print("Total Contributions: ₹{:.2f}".format(total_invested))
        print("Estimated Value After 12 Months: ₹{:.2f}".format(
            estimated_value
        ))
        print("Estimated Gain or Loss: ₹{:.2f}".format(estimated_gain))

    print("\nMonthly Budget Summary :")
    print("Monthly Income: ₹{:.2f}".format(annual_income / 12))
    print("Monthly Tax Estimate: ₹{:.2f}".format(tax_amount / 12))
    print("Monthly Expenses: ₹{:.2f}".format(annual_expenses / 12))
    print("Monthly Disposable Income: ₹{:.2f}".format(
        disposable_income / 12
    ))

    print("\nNote: This is an educational estimate, not an actual tax calculation.")
    print("Actual taxes depend on applicable tax rules, deductions, and other factors.")
    print("Investment returns are hypothetical and are not guaranteed.")

    print("\nSimulation completed successfully.")

taxandsavings()