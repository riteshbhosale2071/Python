def polynomialrepresentation():
    print("Polynomial Representation :")

    try:
        n = int(input("Enter the number of terms in the polynomial: "))
    except ValueError:
        print("Invalid input! Enter an integer.")
        return

    if n <= 0:
        print("Number of terms must be greater than zero.")
        return

    terms = {}

    for i in range(n):
        print("\nTerm", i + 1)

        try:
            coefficient = float(input("Enter the coefficient: "))
            exponent = int(input("Enter the exponent of x: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            return

        if exponent in terms:
            terms[exponent] += coefficient
        else:
            terms[exponent] = coefficient

    print("\nPolynomial Representation :")

    sorted_exponents = sorted(terms.keys(), reverse=True)
    polynomial = ""

    for exponent in sorted_exponents:
        coefficient = terms[exponent]

        if coefficient == 0:
            continue

        absolute_coefficient = abs(coefficient)

        if exponent == 0:
            term = str(absolute_coefficient)
        elif exponent == 1:
            if absolute_coefficient == 1:
                term = "x"
            else:
                term = str(absolute_coefficient) + "x"
        else:
            if absolute_coefficient == 1:
                term = "x^" + str(exponent)
            else:
                term = str(absolute_coefficient) + "x^" + str(exponent)

        if polynomial == "":
            if coefficient < 0:
                polynomial = "-" + term
            else:
                polynomial = term
        else:
            if coefficient < 0:
                polynomial += " - " + term
            else:
                polynomial += " + " + term

    if polynomial == "":
        polynomial = "0"

    print("Polynomial:", polynomial)

    print("\nCoefficient Representation :")
    print("Exponent : Coefficient")

    for exponent in sorted_exponents:
        print(exponent, ":", terms[exponent])

    print("\nPolynomial Analysis :")

    nonzero_exponents = [
        exponent for exponent in sorted_exponents
        if terms[exponent] != 0
    ]

    if len(nonzero_exponents) == 0:
        print("The polynomial is zero.")
    else:
        degree = max(nonzero_exponents)
        print("Degree of Polynomial:", degree)
        print("Number of Nonzero Terms:", len(nonzero_exponents))

        if degree == 0:
            print("Classification: Constant Polynomial")
        elif degree == 1:
            print("Classification: Linear Polynomial")
        elif degree == 2:
            print("Classification: Quadratic Polynomial")
        elif degree == 3:
            print("Classification: Cubic Polynomial")
        else:
            print("Classification: Polynomial of Degree", degree)

polynomialrepresentation()