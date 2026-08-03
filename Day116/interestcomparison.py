def interestcomparison():
    principal = float(input("Enter the principal amount: "))
    rate1 = float(input("Enter the first interest rate (%): "))
    rate2 = float(input("Enter the second interest rate (%): "))
    time = float(input("Enter the time period (in years): "))

    interest1 = (principal * rate1 * time) / 100
    interest2 = (principal * rate2 * time) / 100

    print("Interest at", rate1, "%:", round(interest1, 2))
    print("Interest at", rate2, "%:", round(interest2, 2))

    if interest1 > interest2:
        print("First interest rate gives higher interest.")
    elif interest2 > interest1:
        print("Second interest rate gives higher interest.")
    else:
        print("Both interest rates give the same interest.")

interestcomparison()