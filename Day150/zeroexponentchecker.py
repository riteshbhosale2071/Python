def zeroexponentchecker():
    print("Zero Exponent Checker :")

    base = float(input("Enter the base: "))

    if base == 0:
        print("0^0 is undefined in this program.")
    else:
        result = base ** 0

        print("\nResult :")
        print("Base:", base)
        print("Exponent: 0")
        print("Value:", result)

        if result == 1:
            print("Any non-zero number raised to the power 0 is 1.")

zeroexponentchecker()