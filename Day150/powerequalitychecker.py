def powerequalitychecker():
    print("Power Equality Checker :")

    base1 = float(input("Enter first base: "))
    exponent1 = int(input("Enter first exponent: "))

    base2 = float(input("Enter second base: "))
    exponent2 = int(input("Enter second exponent: "))

    if base1 == 0 and exponent1 <= 0:
        print("Invalid first power.")
        return

    if base2 == 0 and exponent2 <= 0:
        print("Invalid second power.")
        return

    value1 = base1 ** exponent1
    value2 = base2 ** exponent2

    print("\nPower Equality Analysis :")
    print("First Power:", base1, "^", exponent1, "=", value1)
    print("Second Power:", base2, "^", exponent2, "=", value2)

    if abs(value1 - value2) < 1e-9:
        print("The two powers are Equal.")
    else:
        print("The two powers are Not Equal.")

powerequalitychecker()