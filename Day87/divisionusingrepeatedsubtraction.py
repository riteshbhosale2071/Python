def repeatedsub():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    if divisor <= 0:
        print("Divisor must be greater than 0.")
        return

    quotient = 0
    remainder = dividend

    print("\nRepeated Subtraction Steps")
    print("-" * 35)

    while remainder >= divisor:
        print(remainder, "-", divisor, "=", remainder - divisor)
        remainder -= divisor
        quotient += 1

    print("-" * 35)
    print("Quotient =", quotient)
    print("Remainder =", remainder)

repeatedsub()