def dividendincomecalculator():
    try:
        company_name = input("Enter company name: ")
        shares = int(input("Enter number of shares owned: "))
        dividend_per_share = float(input("Enter dividend per share (₹): "))
        dividend_frequency = int(input("Enter number of dividend payments per year: "))

        if shares <= 0 or dividend_per_share < 0 or dividend_frequency <= 0:
            print("Please enter valid investment details.")
            return

        dividend_per_payment = shares * dividend_per_share
        annual_dividend = dividend_per_payment * dividend_frequency

        print("\nDividend Income Report")
        print("Company Name:", company_name)
        print("Total Shares:", shares)
        print("Dividend Per Share: ₹", round(dividend_per_share, 2))
        print("Dividend Payments Per Year:", dividend_frequency)
        print("Income Per Payment: ₹", round(dividend_per_payment, 2))
        print("Annual Dividend Income: ₹", round(annual_dividend, 2))

    except ValueError:
        print("Please enter valid numeric values.")

dividendincomecalculator()