def polynomialremainderextractor():
    print("Polynomial Remainder Extractor :")

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
        print("The remainder is the dividend itself.")

        for i in range(len(dividend)):
            power = dividend_degree - i
            coefficient = round(dividend[i], 2)

            print("Coefficient of x^" + str(power) + ":", coefficient)

        return

    quotient_degree = dividend_degree - divisor_degree
    remainder = dividend[:]

    for i in range(quotient_degree + 1):
        factor = remainder[i] / divisor[0]

        for j in range(divisor_degree + 1):
            remainder[i + j] -= factor * divisor[j]

    remainder_start = quotient_degree + 1

    print("\nRemainder Polynomial Coefficients:")

    has_remainder = False

    for i in range(remainder_start, len(remainder)):
        power = len(remainder) - i - 1
        coefficient = round(remainder[i], 2)

        print("Coefficient of x^" + str(power) + ":", coefficient)

        if coefficient != 0:
            has_remainder = True

    if has_remainder:
        print("The polynomial has a non-zero remainder.")
    else:
        print("The remainder is zero.")

polynomialremainderextractor()