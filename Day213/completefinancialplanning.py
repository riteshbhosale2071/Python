def completefinancialplanning():
    print("Complete Financial Planning Calculator")

    monthly_income = float(input("Enter monthly income: "))
    monthly_expenses = float(input("Enter monthly expenses: "))
    monthly_savings = float(input("Enter monthly savings: "))
    current_savings = float(input("Enter current savings: "))
    monthly_investment = float(input("Enter monthly investment: "))
    investment_return = float(input("Enter expected annual investment return (%): "))
    inflation_rate = float(input("Enter expected annual inflation rate (%): "))
    retirement_years = int(input("Enter years until retirement: "))
    financial_goal = float(input("Enter your financial goal amount: "))

    if min(monthly_income, monthly_expenses, monthly_savings,
           current_savings, monthly_investment, investment_return,
           inflation_rate, financial_goal) < 0 or retirement_years <= 0:
        print("Invalid input. Values cannot be negative and years must be positive.")
        return

    monthly_balance = monthly_income - monthly_expenses
    annual_income = monthly_income * 12
    annual_expenses = monthly_expenses * 12
    annual_savings = monthly_savings * 12
    savings_rate = (monthly_savings / monthly_income * 100) if monthly_income else 0

    monthly_rate = investment_return / 1200
    total_months = retirement_years * 12

    if monthly_rate > 0:
        future_investment = monthly_investment * (
            ((1 + monthly_rate) ** total_months - 1) / monthly_rate
        )
        future_savings = current_savings * ((1 + monthly_rate) ** total_months)
    else:
        future_investment = monthly_investment * total_months
        future_savings = current_savings

    total_future_value = future_investment + future_savings
    inflation_adjusted_goal = financial_goal * (
        (1 + inflation_rate / 100) ** retirement_years
    )

    if monthly_investment > 0:
        required_monthly_investment = (
            inflation_adjusted_goal - future_savings
        ) * monthly_rate / (
            (1 + monthly_rate) ** total_months - 1
        ) if monthly_rate > 0 else (
            inflation_adjusted_goal - current_savings
        ) / total_months
    else:
        required_monthly_investment = 0

    print("\nFinancial Planning Report :")
    print(f"Annual Income: {annual_income:.2f}")
    print(f"Annual Expenses: {annual_expenses:.2f}")
    print(f"Monthly Balance: {monthly_balance:.2f}")
    print(f"Annual Savings: {annual_savings:.2f}")
    print(f"Savings Rate: {savings_rate:.2f}%")
    print(f"Future Value of Investments: {future_investment:.2f}")
    print(f"Future Value of Current Savings: {future_savings:.2f}")
    print(f"Projected Total Wealth: {total_future_value:.2f}")
    print(f"Inflation-Adjusted Financial Goal: {inflation_adjusted_goal:.2f}")
    print(f"Required Monthly Investment: {required_monthly_investment:.2f}")

    if total_future_value >= inflation_adjusted_goal:
        print("Status: Your projected wealth meets your financial goal.")
    else:
        print("Status: Your projected wealth is below your financial goal.")

    if monthly_balance < 0:
        print("Suggestion: Reduce expenses or increase income.")
    elif savings_rate < 20:
        print("Suggestion: Try to increase your monthly savings rate.")
    else:
        print("Suggestion: Maintain your savings discipline.")

completefinancialplanning()