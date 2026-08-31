def ratefinderfrominterest():
    interest = float(input("Enter the simple interest: "))
    principal = float(input("Enter the principal amount: "))
    time = float(input("Enter the time (years): "))

    if interest < 0 or principal <= 0 or time <= 0:
        print("Enter valid values.")
        return

    rate = (interest * 100) / (principal * time)

    print("Interest Rate:", rate, "%")

ratefinderfrominterest()