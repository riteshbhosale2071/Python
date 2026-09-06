def missingpower():
    print("Missing Power Finder :")

    base = float(input("Enter the base: "))
    first_exponent = int(input("Enter first exponent: "))
    second_exponent = int(input("Enter second exponent: "))

    if base == 0:
        print("Base cannot be zero.")
        return

    if first_exponent == second_exponent:
        print("Exponents must be different.")
        return

    first_value = base ** first_exponent
    second_value = base ** second_exponent

    print("\nPower Sequence :")
    print(f"{base}^{first_exponent} =", first_value)
    print(f"{base}^{second_exponent} =", second_value)

    exponent_step = abs(second_exponent - first_exponent)

    print("\nMissing Power Exponent:", exponent_step)
    print("Power Difference:", abs(second_value - first_value))

missingpower()