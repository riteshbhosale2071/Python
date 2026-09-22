def polynomialquotientextractor():
    print("Polynomial Quotient Extractor :")

    dividend_degree = int(input("Enter the degree of the dividend: "))

    dividend = []

    print("Enter dividend coefficients from highest degree to constant:")
    for i in range(dividend_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        dividend.append(coefficient)

    divisor_degree = int(input("Enter the degree of the divisor: "))

    divisor = []

    print("Enter divisor coefficients from highest degree to constant:")
    for i in range(divisor_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        divisor.append(coefficient)

    if divisor[0] == 0:
        print("The leading coefficient of the divisor cannot be zero.")
        return

    if dividend_degree < divisor_degree:
        print("The dividend degree must be greater than or equal to the divisor degree.")
        return

    quotient_degree = dividend_degree - divisor_degree
    quotient = []

    for i in range(quotient_degree + 1):
        quotient.append(0)

    remainder = dividend[:]

    for i in range(quotient_degree + 1):
        factor = remainder[i] / divisor[0]
        quotient[i] = factor

        for j in range(divisor_degree + 1):
            remainder[i + j] -= factor * divisor[j]

    print("\nQuotient Polynomial Coefficients:")

    for i in range(len(quotient)):
        power = quotient_degree - i
        coefficient = round(quotient[i], 2)

        print("Coefficient of x^" + str(power) + ":", coefficient)

    print("\nQuotient Polynomial:")

    expression = ""

    for i in range(len(quotient)):
        coefficient = round(quotient[i], 2)
        power = quotient_degree - i

        if coefficient != 0:
            if expression != "" and coefficient > 0:
                expression += " + "
            elif expression != "" and coefficient < 0:
                expression += " - "

            absolute_coefficient = abs(coefficient)

            if power == 0:
                term = str(absolute_coefficient)
            elif power == 1:
                if absolute_coefficient == 1:
                    term = "x"
                else:
                    term = str(absolute_coefficient) + "x"
            else:
                if absolute_coefficient == 1:
                    term = "x^" + str(power)
                else:
                    term = str(absolute_coefficient) + "x^" + str(power)

            expression += term

    if expression == "":
        expression = "0"

    print(expression)

polynomialquotientextractor()