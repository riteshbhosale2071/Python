def fixeddeposit():
    principal = float(input("Enter the deposit amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time period (in years): "))

    interest = (principal * rate * time) / 100
    maturity_amount = principal + interest

    print("Interest Earned:", round(interest, 2))
    print("Maturity Amount:", round(maturity_amount, 2))

fixeddeposit()