def sparsepolynomial():
    print("Sparse Polynomial Representation :")

    polynomial = input("Enter polynomial: ")
    polynomial = polynomial.replace(" ", "")

    terms = polynomial.replace("-", "+-").split("+")
    sparse = []

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

        sparse.append((power, coefficient))

    print("\nSparse Polynomial Representation :")

    sparse.sort(reverse=True)

    for term in sparse:
        print("Power:", term[0], "Coefficient:", term[1])

    print("\nAs pairs:")
    print(sparse)

sparsepolynomial()