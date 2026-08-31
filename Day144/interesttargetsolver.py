def interesttargetsolver():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter interest rate (%): "))
    target_interest = float(input("Enter target interest: "))

    if principal <= 0 or rate <= 0 or target_interest < 0:
        print("Enter valid values.")
        return

    time = (target_interest * 100) / (principal * rate)

    print("Time required to reach target interest:", time, "years")

interesttargetsolver()