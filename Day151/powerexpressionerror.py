def powerexpressionerror():
    print("Power Expression Error Detector :")

    base = float(input("Enter the base: "))
    exponent1 = int(input("Enter first exponent: "))
    exponent2 = int(input("Enter second exponent: "))

    print("\nChoose the expression rule to validate:")
    print("1. Product Rule: a^m × a^n = a^(m+n)")
    print("2. Quotient Rule: a^m ÷ a^n = a^(m-n)")
    print("3. Power Rule: (a^m)^n = a^(m×n)")
    print("4. Zero Exponent: a^0 = 1")
    print("5. Negative Exponent: a^(-n) = 1/a^n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        left = (base ** exponent1) * (base ** exponent2)
        correct_exponent = exponent1 + exponent2
        right = base ** correct_exponent
        rule = "Product Rule"

    elif choice == 2:
        if base == 0:
            print("Base cannot be zero for division.")
            return

        left = (base ** exponent1) / (base ** exponent2)
        correct_exponent = exponent1 - exponent2
        right = base ** correct_exponent
        rule = "Quotient Rule"

    elif choice == 3:
        left = (base ** exponent1) ** exponent2
        correct_exponent = exponent1 * exponent2
        right = base ** correct_exponent
        rule = "Power Rule"

    elif choice == 4:
        if base == 0:
            print("0^0 is undefined.")
            return

        left = base ** 0
        correct_exponent = 0
        right = 1
        rule = "Zero Exponent Rule"

    elif choice == 5:
        if base == 0 or exponent1 <= 0:
            print("Base must be non-zero and exponent must be positive.")
            return

        left = base ** (-exponent1)
        correct_exponent = -exponent1
        right = 1 / (base ** exponent1)
        rule = "Negative Exponent Rule"

    else:
        print("Invalid choice.")
        return

    print("\nError Detection :")
    print("Rule:", rule)
    print("Left Side:", left)
    print("Correct Right Side:", right)

    if abs(left - right) < 1e-9:
        print("Result: No error detected.")
        print("The power expression follows the selected exponent rule.")
    else:
        print("Result: Error detected.")
        print("The power expression does not follow the selected rule.")

powerexpressionerror()