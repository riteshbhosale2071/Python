def powerexpressionsimplifier():
    print("Power Expression Simplifier :")

    base = float(input("Enter the common base: "))
    exponent1 = int(input("Enter first exponent: "))
    exponent2 = int(input("Enter second exponent: "))

    if base == 0 and (exponent1 < 0 or exponent2 < 0):
        print("Zero cannot have a negative exponent.")
        return

    print("\nChoose operation:")
    print("1. Multiplication  (a^m × a^n)")
    print("2. Division        (a^m ÷ a^n)")
    print("3. Power of Power  ((a^m)^n)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        result_exponent = exponent1 + exponent2
        expression = f"{base}^{exponent1} × {base}^{exponent2}"

    elif choice == 2:
        if exponent1 == 0 and exponent2 == 0:
            print("0^0 is undefined.")
            return

        result_exponent = exponent1 - exponent2
        expression = f"{base}^{exponent1} ÷ {base}^{exponent2}"

    elif choice == 3:
        result_exponent = exponent1 * exponent2
        expression = f"({base}^{exponent1})^{exponent2}"

    else:
        print("Invalid choice.")
        return

    result = base ** result_exponent

    print("\nSimplified Expression :")
    print("Original Expression:", expression)
    print("Simplified Expression:", f"{base}^{result_exponent}")
    print("Value:", result)

powerexpressionsimplifier()