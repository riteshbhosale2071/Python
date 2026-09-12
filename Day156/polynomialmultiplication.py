def polynomialmultiplication():
    print("Polynomial Multiplication Engine :")

    polynomial1 = input("Enter first polynomial: ")
    polynomial2 = input("Enter second polynomial: ")

    polynomial1 = polynomial1.replace(" ", "")
    polynomial2 = polynomial2.replace(" ", "")

    terms1 = polynomial1.replace("-", "+-").split("+")
    terms2 = polynomial2.replace("-", "+-").split("+")

    coefficients1 = {}
    coefficients2 = {}

    for term in terms1:
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

        coefficients1[power] = coefficient

    for term in terms2:
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

        coefficients2[power] = coefficient

    result = {}

    for power1 in coefficients1:
        for power2 in coefficients2:
            power = power1 + power2
            value = coefficients1[power1] * coefficients2[power2]

            if power in result:
                result[power] = result[power] + value
            else:
                result[power] = value

    print("\nPolynomial Product :")

    powers = list(result.keys())
    powers.sort(reverse=True)

    answer = ""

    for power in powers:
        coefficient = result[power]

        if coefficient == 0:
            continue

        if answer == "":
            if coefficient < 0:
                answer = "-"
                coefficient = -coefficient
        else:
            if coefficient > 0:
                answer = answer + " + "
            else:
                answer = answer + " - "
                coefficient = -coefficient

        if power == 0:
            answer = answer + str(coefficient)
        elif power == 1:
            if coefficient == 1:
                answer = answer + "x"
            else:
                answer = answer + str(coefficient) + "x"
        else:
            if coefficient == 1:
                answer = answer + "x^" + str(power)
            else:
                answer = answer + str(coefficient) + "x^" + str(power)

    if answer == "":
        answer = "0"

    print(answer)

polynomialmultiplication()