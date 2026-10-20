def polynomialmultiplication():
    print("Polynomial Multiplication :")

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

    def display_polynomial(polynomial):
        terms = []

        for exponent in sorted(polynomial.keys(), reverse=True):
            coefficient = polynomial[exponent]

            if coefficient == 0:
                continue

            absolute_coefficient = abs(coefficient)

            if exponent == 0:
                term = str(absolute_coefficient)
            elif exponent == 1:
                term = "x" if absolute_coefficient == 1 else str(absolute_coefficient) + "x"
            else:
                term = "x^" + str(exponent) if absolute_coefficient == 1 else str(absolute_coefficient) + "x^" + str(exponent)

            if not terms:
                terms.append("-" + term if coefficient < 0 else term)
            else:
                terms.append((" - " if coefficient < 0 else " + ") + term)

        return "".join(terms) if terms else "0"

    polynomial_a = input_polynomial("Polynomial A")

    if polynomial_a is None:
        return

    polynomial_b = input_polynomial("Polynomial B")

    if polynomial_b is None:
        return

    result = {}

    for exponent_a, coefficient_a in polynomial_a.items():
        for exponent_b, coefficient_b in polynomial_b.items():
            new_exponent = exponent_a + exponent_b
            new_coefficient = coefficient_a * coefficient_b

            if new_exponent in result:
                result[new_exponent] += new_coefficient
            else:
                result[new_exponent] = new_coefficient

    print("\nPolynomial Multiplication Results :")
    print("Polynomial A:", display_polynomial(polynomial_a))
    print("Polynomial B:", display_polynomial(polynomial_b))
    print("Product:", display_polynomial(result))

    print("\nMultiplication Details :")

    for exponent_a, coefficient_a in polynomial_a.items():
        for exponent_b, coefficient_b in polynomial_b.items():
            print(
                coefficient_a, "x^", exponent_a,
                "×", coefficient_b, "x^", exponent_b,
                "=", coefficient_a * coefficient_b,
                "x^", exponent_a + exponent_b
            )

    nonzero_exponents = [
        exponent for exponent, coefficient in result.items()
        if coefficient != 0
    ]

    print("\nFinal Analysis :")

    if nonzero_exponents:
        print("Degree of Product:", max(nonzero_exponents))
        print("Number of Nonzero Terms:", len(nonzero_exponents))
    else:
        print("The product is the zero polynomial.")

polynomialmultiplication()