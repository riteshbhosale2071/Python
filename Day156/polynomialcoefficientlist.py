def polynomialcoefficientlist():
    print("Polynomial Coefficient List Generator :")

    polynomial = input("Enter a polynomial: ")
    polynomial = polynomial.replace(" ", "")

    coefficients = []
    i = 0

    while i < len(polynomial):
        sign = 1

        if polynomial[i] == "+":
            sign = 1
            i = i + 1
        elif polynomial[i] == "-":
            sign = -1
            i = i + 1

        number = ""

        while i < len(polynomial) and polynomial[i].isdigit():
            number = number + polynomial[i]
            i = i + 1

        if i < len(polynomial) and polynomial[i] == "x":
            if number == "":
                number = "1"

            coefficient = sign * int(number)
            coefficients.append(coefficient)
            i = i + 1

            if i < len(polynomial) and polynomial[i] == "^":
                i = i + 1

                while i < len(polynomial) and polynomial[i].isdigit():
                    i = i + 1
        else:
            if number != "":
                coefficient = sign * int(number)
                coefficients.append(coefficient)

    print("\nCoefficient List:")
    print(coefficients)

polynomialcoefficientlist()