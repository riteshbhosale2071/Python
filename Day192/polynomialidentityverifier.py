def polynomialidentityverifier():
    print("Polynomial Identity Verifier :")

    def input_polynomial(name):
        try:
            n = int(input("Enter the number of terms in " + name + ": "))
        except ValueError:
            print("Invalid input! Enter an integer.")
            return None

        if n < 0:
            print("Number of terms cannot be negative.")
            return None

        polynomial = {}

        for i in range(n):
            print("\n" + name + " - Term", i + 1)

            try:
                coefficient = float(input("Enter coefficient: "))
                exponent = int(input("Enter exponent of x: "))
            except ValueError:
                print("Invalid input! Enter valid numbers.")
                return None

            if exponent < 0:
                print("Exponent must be a non-negative integer.")
                return None

            if exponent in polynomial:
                polynomial[exponent] += coefficient
            else:
                polynomial[exponent] = coefficient

        return polynomial

    polynomial_a = input_polynomial("Polynomial A")

    if polynomial_a is None:
        return

    polynomial_b = input_polynomial("Polynomial B")

    if polynomial_b is None:
        return

    all_exponents = set(polynomial_a.keys()) | set(polynomial_b.keys())
    identical = True

    print("\n=== Coefficient Comparison ===")

    for exponent in sorted(all_exponents, reverse=True):
        coefficient_a = polynomial_a.get(exponent, 0)
        coefficient_b = polynomial_b.get(exponent, 0)

        print(
            "Exponent:", exponent,
            "| Polynomial A:", coefficient_a,
            "| Polynomial B:", coefficient_b
        )

        if abs(coefficient_a - coefficient_b) > 1e-9:
            identical = False

    print("\nIdentity Verification Results :")

    if identical:
        print("Result: Both polynomials are identical.")
        print("The identity is verified for every value of x.")
    else:
        print("Result: The polynomials are not identical.")
        print("Their coefficients differ for at least one exponent.")

    try:
        x = float(input("\nEnter a value of x for additional testing: "))
    except ValueError:
        print("Invalid input! Skipping numerical testing.")
        return

    value_a = 0
    value_b = 0

    for exponent, coefficient in polynomial_a.items():
        value_a += coefficient * (x ** exponent)

    for exponent, coefficient in polynomial_b.items():
        value_b += coefficient * (x ** exponent)

    print("\nNumerical Verification :")
    print("Value of x:", x)
    print("Polynomial A Value:", round(value_a, 6))
    print("Polynomial B Value:", round(value_b, 6))

    if abs(value_a - value_b) <= 1e-9:
        print("Both polynomials have equal values at this point.")
    else:
        print("The polynomial values differ at this point.")

polynomialidentityverifier()