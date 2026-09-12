def polynomialevaluation():
    print("Polynomial Evaluation Program :")

    polynomial = input("Enter polynomial: ")
    x = float(input("Enter value of x: "))

    polynomial = polynomial.replace(" ", "")
    terms = polynomial.replace("-", "+-").split("+")

    result = 0

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

            result = result + coefficient * (x ** power)

        elif "x" in term:
            parts = term.split("x")

            if parts[0] == "":
                coefficient = 1
            elif parts[0] == "-":
                coefficient = -1
            else:
                coefficient = int(parts[0])

            result = result + coefficient * x

        else:
            result = result + int(term)

    print("\nPolynomial value:", result)

polynomialevaluation()