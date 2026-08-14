def powercomparison():
    base1 = float(input("Enter the base of first power: "))
    exponent1 = float(input("Enter the exponent of first power: "))

    base2 = float(input("Enter the base of second power: "))
    exponent2 = float(input("Enter the exponent of second power: "))

    if base1 == 0 and exponent1 <= 0 or base2 == 0 and exponent2 <= 0:
        print("Invalid power expression.")
        return

    value1 = base1 ** exponent1
    value2 = base2 ** exponent2

    print(f"First Power: {value1}")
    print(f"Second Power: {value2}")

    if value1 > value2:
        print("First power is greater.")
    elif value1 < value2:
        print("Second power is greater.")
    else:
        print("Both powers are equal.")

powercomparison()