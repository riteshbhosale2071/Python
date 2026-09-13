def polynomialcoefficientsearch():
    print("Polynomial Coefficient Search :")

    polynomial = input("Enter polynomial: ")
    power_search = int(input("Enter power to search: "))

    polynomial = polynomial.replace(" ", "")
    terms = polynomial.replace("-", "+-").split("+")

    found = False
    coefficient_result = 0

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

        if power == power_search:
            coefficient_result = coefficient_result + coefficient
            found = True

    print("\nSearch Result :")

    if found:
        print("Power:", power_search)
        print("Coefficient:", coefficient_result)
    else:
        print("No term with power", power_search, "was found.")

polynomialcoefficientsearch()