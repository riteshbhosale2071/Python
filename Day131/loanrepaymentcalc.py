def loanrepaymentcalc():
    principal = float(input("Enter loan amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter loan period (years): "))

    if principal <= 0 or rate < 0 or time <= 0:
        print("Please enter valid values.")
        return

    if rate == 0:
        total_amount = principal
    else:
        interest = (principal * rate * time) / 100
        total_amount = principal + interest

    print("Loan Amount:", principal)
    print("Total Repayment Amount:", total_amount)
    print("Monthly Repayment:", total_amount / (time * 12))

loanrepaymentcalc()