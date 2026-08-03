def loaninterest():
    loan_amount = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the loan period (in years): "))

    interest = (loan_amount * rate * time) / 100
    total_payment = loan_amount + interest

    print("Loan Interest:", round(interest, 2))
    print("Total Amount to Repay:", round(total_payment, 2))

loaninterest()