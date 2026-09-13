def polynomialcomparison():
    print("Polynomial Comparison Tool :")

    polynomial1 = input("Enter first polynomial: ")
    polynomial2 = input("Enter second polynomial: ")

    polynomial1 = polynomial1.replace(" ", "")
    polynomial2 = polynomial2.replace(" ", "")

    def get_coefficients(polynomial):
        terms = polynomial.replace("-", "+-").split("+")
        coefficients = {}

        for term in terms:
            if term == "":
                continue

            if "x^" in term:
                parts = term.split("x^")
                coefficient = parts[0]
                power = int(parts[1])

                if coefficient == "":
                    coefficient = 1
                elif coefficient == "-":
                    coefficient = -1
                else:
                    coefficient = int(coefficient)

            elif "x" in term:
                parts = term.split("x")

                if parts[0] == "":
                    coefficient = 1
                elif parts[0] == "-":
                    coefficient = -1
                else:
                    coefficient = int(parts[0])

                power = 1

            else:
                coefficient = int(term)
                power = 0

            if power in coefficients:
                coefficients[power] = coefficients[power] + coefficient
            else:
                coefficients[power] = coefficient

        return coefficients

    coefficients1 = get_coefficients(polynomial1)
    coefficients2 = get_coefficients(polynomial2)

    powers = list(coefficients1.keys())

    for power in coefficients2:
        if power not in powers:
            powers.append(power)

    powers.sort(reverse=True)

    same = True

    print("\nPolynomial Comparison :")

    for power in powers:
        value1 = coefficients1.get(power, 0)
        value2 = coefficients2.get(power, 0)

        print("x^" + str(power) + ":", value1, "vs", value2)

        if value1 != value2:
            same = False

    if same:
        print("\nThe two polynomials are equal.")
    else:
        print("\nThe two polynomials are different.")

polynomialcomparison()