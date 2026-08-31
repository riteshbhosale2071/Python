def timefinderfrominterest():
    interest = float(input("Enter the simple interest: "))
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate (%): "))

    if interest < 0 or principal <= 0 or rate <= 0:
        print("Enter valid values.")
        return

    time = (interest * 100) / (principal * rate)

    print("Time:", time, "years")

timefinderfrominterest()