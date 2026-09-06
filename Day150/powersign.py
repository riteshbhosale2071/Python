def powersign():
    print("Power Sign Analyzer :")

    base = float(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))

    if base == 0:
        if exponent > 0:
            print("Result: 0")
        elif exponent == 0:
            print("0^0 is undefined.")
        else:
            print("0 cannot have a negative exponent.")
        return

    result = base ** exponent

    print("\nPower Sign Analysis :")
    print("Base:", base)
    print("Exponent:", exponent)
    print("Result:", result)

    if result > 0:
        print("Sign: Positive")
    elif result < 0:
        print("Sign: Negative")
    else:
        print("Sign: Zero")

powersign()