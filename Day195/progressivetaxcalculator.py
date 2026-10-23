def progressivetaxcalculator():
    print("Progressive Tax Calculator :")

    try:
        income = float(input("Enter your annual taxable income: "))
        n = int(input("Enter the number of tax slabs: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if income < 0:
        print("Income cannot be negative.")
        return

    if n <= 0:
        print("Number of tax slabs must be greater than zero.")
        return

    slabs = []

    print("\nEnter each slab's upper income limit and tax rate.")
    print("For the final slab, enter -1 as the upper limit for unlimited income.")

    for i in range(n):
        print("\nTax Slab", i + 1)

        try:
            upper_limit = float(input("Enter upper income limit: "))
            rate = float(input("Enter tax rate (%): "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return

        if upper_limit == -1:
            if i != n - 1:
                print("The unlimited slab must be the final slab.")
                return
        elif upper_limit <= 0:
            print("Upper income limit must be positive or -1.")
            return

        if rate < 0 or rate > 100:
            print("Tax rate must be between 0 and 100.")
            return

        if slabs and upper_limit != -1 and upper_limit <= slabs[-1][0]:
            print("Income limits must be in increasing order.")
            return

        slabs.append((upper_limit, rate))

    if slabs[-1][0] != -1 and income > slabs[-1][0]:
        print("The final tax slab must cover the entered income.")
        return

    tax = 0
    previous_limit = 0
    remaining_income = income

    print("\nProgressive Tax Calculation :")
    print("Annual Taxable Income:", round(income, 2))

    for i, (upper_limit, rate) in enumerate(slabs):
        if remaining_income <= 0:
            break

        if upper_limit == -1:
            taxable_amount = remaining_income
        else:
            slab_width = upper_limit - previous_limit
            taxable_amount = min(remaining_income, slab_width)

        slab_tax = taxable_amount * rate / 100
        tax += slab_tax

        if upper_limit == -1:
            slab_description = str(previous_limit) + " and above"
        else:
            slab_description = str(previous_limit) + " to " + str(upper_limit)

        print("\nSlab", i + 1, ":", slab_description)
        print("Tax Rate:", rate, "%")
        print("Income Taxed in Slab:", round(taxable_amount, 2))
        print("Tax for Slab:", round(slab_tax, 2))

        remaining_income -= taxable_amount

        if upper_limit != -1:
            previous_limit = upper_limit

    print("\nFinal Tax Summary :")
    print("Total Taxable Income:", round(income, 2))
    print("Total Progressive Tax:", round(tax, 2))
    print("Income After Tax:", round(income - tax, 2))

    if income > 0:
        effective_rate = (tax / income) * 100
        print("Effective Tax Rate:", round(effective_rate, 2), "%")
    else:
        print("Effective Tax Rate: 0.00%")

    print("\nNote: Tax is calculated separately for each income slab.")
    print("This is a general calculator, not a country-specific tax estimate.")

progressivetaxcalculator()