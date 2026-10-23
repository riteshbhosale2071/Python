def calculateprogressivetax(income, slabs):
    tax = 0
    previous_limit = 0
    details = []

    for upper_limit, rate in slabs:
        if income <= previous_limit:
            break

        if upper_limit == -1:
            taxable_amount = income - previous_limit
        else:
            taxable_amount = min(income, upper_limit) - previous_limit

        if taxable_amount > 0:
            slab_tax = taxable_amount * rate / 100
            tax += slab_tax
            details.append((taxable_amount, rate, slab_tax))

        if upper_limit == -1 or income <= upper_limit:
            break

        previous_limit = upper_limit

    return tax, details


def taxcomparison():
    print("Tax Comparison Tool :")

    try:
        income = float(input("Enter annual taxable income: "))
    except ValueError:
        print("Invalid input! Please enter a numeric income.")
        return

    if income < 0:
        print("Income cannot be negative.")
        return

    regimes = []

    try:
        count = int(input("Enter the number of tax regimes to compare: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if count < 2:
        print("Enter at least two tax regimes for comparison.")
        return

    for i in range(count):
        print("\nEnter details for Tax Regime", i + 1)
        name = input("Enter regime name: ")

        try:
            n = int(input("Enter the number of tax slabs: "))
        except ValueError:
            print("Invalid number of slabs.")
            return

        if n <= 0:
            print("Number of slabs must be greater than zero.")
            return

        slabs = []

        for j in range(n):
            print("\nSlab", j + 1)

            try:
                upper_limit = float(
                    input("Enter upper income limit (-1 for unlimited): ")
                )
                rate = float(input("Enter tax rate (%): "))
            except ValueError:
                print("Invalid slab input.")
                return

            if upper_limit != -1 and upper_limit <= 0:
                print("Upper limit must be positive or -1.")
                return

            if rate < 0 or rate > 100:
                print("Tax rate must be between 0 and 100.")
                return

            if slabs and upper_limit != -1:
                if slabs[-1][0] == -1 or upper_limit <= slabs[-1][0]:
                    print("Slab limits must be in increasing order.")
                    return

            if upper_limit == -1 and j != n - 1:
                print("Unlimited slab must be the final slab.")
                return

            slabs.append((upper_limit, rate))

        if slabs[-1][0] != -1 and income > slabs[-1][0]:
            print("The final slab must cover the entered income.")
            return

        tax, details = calculateprogressivetax(income, slabs)
        regimes.append({
            "name": name,
            "tax": tax,
            "details": details
        })

    print("\nTax Comparison Results :")
    print("Annual Taxable Income:", round(income, 2))

    for regime in regimes:
        tax = regime["tax"]
        effective_rate = (tax / income * 100) if income > 0 else 0

        print("\nRegime:", regime["name"])
        print("Calculated Tax:", round(tax, 2))
        print("Income After Tax:", round(income - tax, 2))
        print("Effective Tax Rate:", round(effective_rate, 2), "%")

        print("Slab Breakdown:")
        for amount, rate, slab_tax in regime["details"]:
            print(
                "Income Taxed:", round(amount, 2),
                "| Rate:", rate, "%",
                "| Tax:", round(slab_tax, 2)
            )

    lowest_tax = min(regimes, key=lambda item: item["tax"])
    highest_tax = max(regimes, key=lambda item: item["tax"])

    print("\nComparison Summary :")
    print("Lowest Tax Regime:", lowest_tax["name"])
    print("Lowest Tax Amount:", round(lowest_tax["tax"], 2))
    print("Highest Tax Regime:", highest_tax["name"])
    print("Highest Tax Amount:", round(highest_tax["tax"], 2))
    print(
        "Maximum Tax Difference:",
        round(highest_tax["tax"] - lowest_tax["tax"], 2)
    )

    print("\nNote: This tool compares user-defined tax slabs.")
    print("It does not automatically apply rebates, cess, or deductions.")

taxcomparison()