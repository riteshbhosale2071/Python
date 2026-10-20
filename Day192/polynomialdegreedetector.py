def polynomialdegreedetector():
    print("Polynomial Degree Detector :")

    try:
        n = int(input("Enter the number of terms in the polynomial: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
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

        if exponent < 0:
            print("Invalid exponent! Polynomial exponents must be non-negative integers.")
            return

        if exponent in terms:
            terms[exponent] += coefficient
        else:
            terms[exponent] = coefficient

    nonzero_exponents = []

    for exponent, coefficient in terms.items():
        if coefficient != 0:
            nonzero_exponents.append(exponent)

    print("\nPolynomial Analysis :")

    if len(nonzero_exponents) == 0:
        print("Polynomial: 0")
        print("Degree: Undefined for the zero polynomial.")
        return

    degree = max(nonzero_exponents)

    print("Combined Terms:", terms)
    print("Polynomial Degree:", degree)

    if degree == 0:
        print("Classification: Constant Polynomial")
    elif degree == 1:
        print("Classification: Linear Polynomial")
    elif degree == 2:
        print("Classification: Quadratic Polynomial")
    elif degree == 3:
        print("Classification: Cubic Polynomial")
    else:
        print("Classification: Higher-Degree Polynomial")

    print("\nDegree Verification :")

    for exponent in sorted(nonzero_exponents, reverse=True):
        print("Exponent:", exponent, "| Coefficient:", terms[exponent])

    print("Highest exponent with a nonzero coefficient:", degree)

polynomialdegreedetector()