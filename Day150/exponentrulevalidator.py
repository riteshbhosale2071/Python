def exponentrulevalidator():
    print("Exponent Rule Validator :")

    print("\nChoose an exponent rule:")
    print("1. Product Rule       a^m × a^n = a^(m+n)")
    print("2. Quotient Rule      a^m ÷ a^n = a^(m-n)")
    print("3. Power Rule         (a^m)^n = a^(m×n)")
    print("4. Zero Exponent      a^0 = 1")
    print("5. Negative Exponent  a^(-n) = 1/a^n")

    choice = int(input("\nEnter your choice: "))

    base = float(input("Enter the base: "))

    if choice == 1:
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))

        left = (base ** m) * (base ** n)
        right = base ** (m + n)

    elif choice == 2:
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))

        if base == 0:
            print("Base cannot be zero for division.")
            return

        left = (base ** m) / (base ** n)
        right = base ** (m - n)

    elif choice == 3:
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))

        left = (base ** m) ** n
        right = base ** (m * n)

    elif choice == 4:
        if base == 0:
            print("0^0 is undefined.")
            return

        left = base ** 0
        right = 1

    elif choice == 5:
        n = int(input("Enter n: "))

        if base == 0:
            print("Zero cannot have a negative exponent.")
            return

        if n <= 0:
            print("Enter a positive value for n.")
            return

        left = base ** (-n)
        right = 1 / (base ** n)

    else:
        print("Invalid choice.")
        return

    print("\nExponent Rule Validation :")
    print("Left Side :", left)
    print("Right Side:", right)

    if abs(left - right) < 1e-9:
        print("Result: The exponent rule is VALID.")
    else:
        print("Result: The exponent rule is INVALID.")

exponentrulevalidator()