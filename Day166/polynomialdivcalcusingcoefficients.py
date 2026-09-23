def polynomialdivcalcusingcoefficients():
    print("Polynomial Division Calculator Using Coefficients :")

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
        print("The quotient is zero.")
        print("The remainder is the dividend.")

        for coefficient in dividend:
            print(round(coefficient, 2))

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

    print("\nQuotient Coefficients :")

    for i in range(len(quotient)):
        power = quotient_degree - i
        print("Coefficient of x^" + str(power) + ":", round(quotient[i], 2))

    print("\nRemainder Coefficients :")

    remainder_start = quotient_degree + 1

    for i in range(remainder_start, len(remainder)):
        power = len(remainder) - i - 1
        print("Coefficient of x^" + str(power) + ":", round(remainder[i], 2))

    print("\nPolynomial division completed successfully.")

polynomialdivcalcusingcoefficients()