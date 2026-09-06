def samepowercomparison():
    print("Same-Power Comparison Program :")

    base1 = float(input("Enter first base: "))
    base2 = float(input("Enter second base: "))
    exponent = int(input("Enter common exponent: "))

    if exponent < 0 and (base1 == 0 or base2 == 0):
        print("Zero cannot have a negative exponent.")
        return

    if exponent == 0 and (base1 == 0 or base2 == 0):
        print("0^0 is undefined.")
        return

    value1 = base1 ** exponent
    value2 = base2 ** exponent

    print("\nSame-Power Comparison :")
    print("First Power:", base1, "^", exponent, "=", value1)
    print("Second Power:", base2, "^", exponent, "=", value2)

    if value1 > value2:
        print("First power is Greater.")
    elif value1 < value2:
        print("Second power is Greater.")
    else:
        print("Both powers are Equal.")

samepowercomparison()