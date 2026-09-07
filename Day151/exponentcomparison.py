def exponentcomparison():
    print("Exponent Comparison Engine :")

    print("\nEnter the first power:")
    base1 = float(input("Base: "))
    exponent1 = int(input("Exponent: "))

    print("\nEnter the second power:")
    base2 = float(input("Base: "))
    exponent2 = int(input("Exponent: "))

    # Validate powers
    if base1 == 0 and exponent1 <= 0:
        print("First power is undefined.")
        return

    if base2 == 0 and exponent2 <= 0:
        print("Second power is undefined.")
        return

    value1 = base1 ** exponent1
    value2 = base2 ** exponent2

    print("\nExponent Comparison :")
    print(f"First Power : {base1}^{exponent1} = {value1}")
    print(f"Second Power: {base2}^{exponent2} = {value2}")

    if abs(value1 - value2) < 1e-9:
        print("Result: Both powers are Equal.")
    elif value1 > value2:
        print("Result: First power is Greater.")
    else:
        print("Result: Second power is Greater.")

exponentcomparison()