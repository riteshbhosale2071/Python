def polynomiallongdivision():
    print("Polynomial Long Division Simulator :")

    dividend_degree = int(input("Enter the degree of the dividend: "))

    dividend = []

    print("Enter the dividend coefficients from highest degree to constant:")
    for i in range(dividend_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        dividend.append(coefficient)

    divisor_degree = int(input("Enter the degree of the divisor: "))

    divisor = []

    print("Enter the divisor coefficients from highest degree to constant:")
    for i in range(divisor_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        divisor.append(coefficient)

    if divisor[0] == 0:
        print("The leading coefficient of the divisor cannot be zero.")
        return

    if dividend_degree < divisor_degree:
        print("The degree of the dividend must be greater than or equal to the divisor.")
        return

    quotient = []
    remainder = dividend[:]

    quotient_degree = dividend_degree - divisor_degree

    for i in range(quotient_degree + 1):
        quotient.append(0)

    for i in range(quotient_degree + 1):
        factor = remainder[i] / divisor[0]
        quotient[i] = factor

        for j in range(divisor_degree + 1):
            remainder[i + j] -= factor * divisor[j]

    print("\nQuotient Coefficients:")
    for coefficient in quotient:
        print(round(coefficient, 2))

    print("\nRemainder Coefficients:")
    remainder_start = quotient_degree + 1

    has_remainder = False

    for i in range(remainder_start, len(remainder)):
        value = round(remainder[i], 2)
        print(value)

        if value != 0:
            has_remainder = True

    if has_remainder:
        print("The division has a non-zero remainder.")
    else:
        print("The polynomial divides completely with no remainder.")

polynomiallongdivision()