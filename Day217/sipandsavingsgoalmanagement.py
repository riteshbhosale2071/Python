def sipandsavingsgoalmanagement():
    print("SIP and Savings Goal Management :")

    monthly_sip = float(input("Enter monthly SIP investment: "))
    annual_return = float(input("Enter expected annual return (%): "))
    years = int(input("Enter investment period in years: "))
    current_savings = float(input("Enter current savings: "))
    savings_goal = float(input("Enter your savings goal: "))

    if monthly_sip < 0 or annual_return < 0 or years <= 0 or current_savings < 0 or savings_goal <= 0:
        print("Please enter valid values.")
        return

    months = years * 12
    monthly_rate = annual_return / 1200

    if monthly_rate > 0:
        sip_value = monthly_sip * (((1 + monthly_rate) ** months - 1) / monthly_rate)
        savings_value = current_savings * (1 + monthly_rate) ** months
    else:
        sip_value = monthly_sip * months
        savings_value = current_savings

    total_invested = monthly_sip * months
    maturity_value = sip_value + savings_value
    estimated_profit = sip_value - total_invested

    print("\nSIP and Savings Summary:")
    print("Monthly SIP:", round(monthly_sip, 2))
    print("Total SIP Investment:", round(total_invested, 2))
    print("Current Savings:", round(current_savings, 2))
    print("Estimated SIP Value:", round(sip_value, 2))
    print("Estimated Savings Value:", round(savings_value, 2))
    print("Estimated SIP Profit:", round(estimated_profit, 2))
    print("Total Future Value:", round(maturity_value, 2))
    print("Savings Goal:", round(savings_goal, 2))

    remaining_amount = savings_goal - maturity_value

    if remaining_amount <= 0:
        print("Status: Your savings goal is achievable.")
        print("Amount Above Goal:", round(abs(remaining_amount), 2))
    else:
        print("Status: Your savings goal is not yet achieved.")
        print("Remaining Amount:", round(remaining_amount, 2))

        if monthly_rate > 0:
            required_sip = (
                (savings_goal - savings_value) * monthly_rate
                / ((1 + monthly_rate) ** months - 1)
            )
        else:
            required_sip = (savings_goal - current_savings) / months

        print("Required Monthly SIP:", round(max(0, required_sip), 2))

sipandsavingsgoalmanagement()