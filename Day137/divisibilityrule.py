def divisibilityrule():
    number = int(input("Enter an integer: "))
    divisor = int(input("Enter the divisor: "))

    if divisor == 0:
        print("Divisor cannot be zero.")
        return

    if number % divisor == 0:
        print(f"{number} is divisible by {divisor}.")
    else:
        print(f"{number} is not divisible by {divisor}.")
        print("Remainder:", number % divisor)

divisibilityrule()