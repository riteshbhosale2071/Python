def polynomialremainderchecker():
    print("Polynomial Remainder Checker :")

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
            print("Coefficient of x^" + str(power) + ":", round(dividend[i], 2))

        return

    quotient_degree = dividend_degree - divisor_degree
    remainder = dividend[:]

    for i in range(quotient_degree + 1):
        factor = remainder[i] / divisor[0]

        for j in range(divisor_degree + 1):
            remainder[i + j] -= factor * divisor[j]

    remainder_start = quotient_degree + 1
    has_remainder = False

    print("\nRemainder Coefficients :")

    for i in range(remainder_start, len(remainder)):
        power = len(remainder) - i - 1
        coefficient = round(remainder[i], 2)

        print("Coefficient of x^" + str(power) + ":", coefficient)

        if coefficient != 0:
            has_remainder = True

    if has_remainder:
        print("\nThe polynomial has a non-zero remainder.")
    else:
        print("\nThe polynomial has a zero remainder.")
        print("The dividend is completely divisible by the divisor.")

polynomialremainderchecker()