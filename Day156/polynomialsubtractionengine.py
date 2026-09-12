def polynomialsubtractionengine():
    print("Polynomial Subtraction Engine :")

    polynomial1 = input("Enter first polynomial: ")
    polynomial2 = input("Enter second polynomial: ")

    polynomial1 = polynomial1.replace(" ", "")
    polynomial2 = polynomial2.replace(" ", "")

    terms1 = polynomial1.replace("-", "+-").split("+")
    terms2 = polynomial2.replace("-", "+-").split("+")

    coefficients = {}

    for term in terms1:
        if term == "":
            continue

        if "x^" in term:
            parts = term.split("x^")
            coefficient = parts[0]

            if coefficient == "":
                coefficient = 1
            elif coefficient == "-":
                coefficient = -1
            else:
                coefficient = int(coefficient)

            power = int(parts[1])

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

    for term in terms2:
        if term == "":
            continue

        if "x^" in term:
            parts = term.split("x^")
            coefficient = parts[0]

            if coefficient == "":
                coefficient = 1
            elif coefficient == "-":
                coefficient = -1
            else:
                coefficient = int(coefficient)

            power = int(parts[1])

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
            coefficients[power] = coefficients[power] - coefficient
        else:
            coefficients[power] = -coefficient

    print("\nPolynomial Difference :")

    powers = list(coefficients.keys())
    powers.sort(reverse=True)

    result = ""

    for power in powers:
        coefficient = coefficients[power]

        if coefficient == 0:
            continue

        if result == "":
            if coefficient < 0:
                result = "-"
                coefficient = -coefficient
        else:
            if coefficient > 0:
                result = result + " + "
            else:
                result = result + " - "
                coefficient = -coefficient

        if power == 0:
            result = result + str(coefficient)
        elif power == 1:
            if coefficient == 1:
                result = result + "x"
            else:
                result = result + str(coefficient) + "x"
        else:
            if coefficient == 1:
                result = result + "x^" + str(power)
            else:
                result = result + str(coefficient) + "x^" + str(power)

    if result == "":
        result = "0"

    print(result)

polynomialsubtractionengine()