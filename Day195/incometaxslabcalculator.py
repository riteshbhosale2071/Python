def incometaxslabcalculator():
    print("Income Tax Slab Calculator :")
    print("Choose Tax Regime:")
    print("1. New Tax Regime (FY 2026-27)")
    print("2. Old Tax Regime (individual below 60 years)")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        income = float(input("Enter your annual taxable income (Rs.): "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if income < 0:
        print("Income cannot be negative.")
        return

    if choice not in (1, 2):
        print("Invalid choice! Select 1 or 2.")
        return

    tax = 0

    if choice == 1:
        slabs = [
            (400000, 0),
            (800000, 0.05),
            (1200000, 0.10),
            (1600000, 0.15),
            (2000000, 0.20),
            (2400000, 0.25),
            (float("inf"), 0.30)
        ]

        previous_limit = 0

        for limit, rate in slabs:
            taxable_amount = min(income, limit) - previous_limit

            if taxable_amount > 0:
                tax += taxable_amount * rate

            if income <= limit:
                break

            previous_limit = limit

        print("\nTax Regime: New Tax Regime")
        print("Annual Taxable Income:", round(income, 2))
        print("Tax Before Rebate:", round(tax, 2))

        if income <= 1200000:
            tax = max(0, tax - min(tax, 60000))
            print("Section 87A Rebate Applied: Eligible, subject to conditions")
        elif income <= 1270588:
            rebate = max(0, tax - (income - 1200000))
            tax -= rebate
            print("Marginal Relief:", round(rebate, 2))
        else:
            print("Section 87A Rebate: Not applicable at this income level")

    else:
        slabs = [
            (250000, 0),
            (500000, 0.05),
            (1000000, 0.20),
            (float("inf"), 0.30)
        ]

        previous_limit = 0

        for limit, rate in slabs:
            taxable_amount = min(income, limit) - previous_limit

            if taxable_amount > 0:
                tax += taxable_amount * rate

            if income <= limit:
                break

            previous_limit = limit

        print("\nTax Regime: Old Tax Regime")
        print("Annual Taxable Income:", round(income, 2))
        print("Tax Before Rebate:", round(tax, 2))

        if income <= 500000:
            rebate = min(tax, 12500)
            tax -= rebate
            print("Section 87A Rebate:", round(rebate, 2))

    cess = tax * 0.04
    total_tax = tax + cess

    print("\nTax Calculation Summary :")
    print("Income Tax After Rebate:", round(tax, 2))
    print("Health and Education Cess (4%):", round(cess, 2))
    print("Estimated Total Tax Payable:", round(total_tax, 2))
    print("Estimated Income After Tax:", round(income - total_tax, 2))

    if income > 0:
        print("Effective Tax Rate:", round((total_tax / income) * 100, 2), "%")
    else:
        print("Effective Tax Rate: 0.00%")

    print("\nNote: This is a simplified estimate for individuals.")
    print("It excludes surcharge, special-rate income, and other adjustments.")
    print("Verify applicable tax rules before filing your return.")

incometaxslabcalculator()