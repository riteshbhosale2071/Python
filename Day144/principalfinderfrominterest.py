def principalfinderfrominterest():
    interest = float(input("Enter the simple interest: "))
    rate = float(input("Enter the interest rate (%): "))
    time = float(input("Enter the time (years): "))

    if interest < 0 or rate <= 0 or time <= 0:
        print("Enter valid values.")
        return

    principal = (interest * 100) / (rate * time)

    print("Principal Amount:", principal)

principalfinderfrominterest()