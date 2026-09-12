def polynomialadditionengine():
    print("Polynomial Addition Engine :")

    polynomial1 = input("Enter first polynomial: ")
    polynomial2 = input("Enter second polynomial: ")

    polynomial1 = polynomial1.replace(" ", "")
    polynomial2 = polynomial2.replace(" ", "")

    terms1 = polynomial1.split("+")
    terms2 = polynomial2.split("+")

    coefficients = {}
    
    for term in terms1:
        if "x^" in term:
            parts = term.split("x^")
            coefficient = int(parts[0])
            power = int(parts[1])
        elif "x" in term:
            parts = term.split("x")
            if parts[0] == "":
                coefficient = 1
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
        if "x^" in term:
            parts = term.split("x^")
            coefficient = int(parts[0])
            power = int(parts[1])
        elif "x" in term:
            parts = term.split("x")
            if parts[0] == "":
                coefficient = 1
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

    print("\nPolynomial Sum :")

    powers = list(coefficients.keys())
    powers.sort(reverse=True)

    result = ""

    for power in powers:
        coefficient = coefficients[power]

        if coefficient == 0:
            continue

        if result != "":
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

polynomialadditionengine()