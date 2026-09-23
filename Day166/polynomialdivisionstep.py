def polynomialdivisionstep():
    print("Polynomial Division Step Generator :")

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

    remainder = dividend[:]
    quotient_degree = dividend_degree - divisor_degree

    print("\nDivision Steps :")

    for step in range(quotient_degree + 1):
        current_power = dividend_degree - step
        factor = remainder[step] / divisor[0]

        print("\nStep", step + 1)
        print("Current Power:", current_power)
        print("Quotient Term:", round(factor, 2), "x^" + str(quotient_degree - step))

        for j in range(divisor_degree + 1):
            remainder[step + j] -= factor * divisor[j]

        print("Updated Remainder Coefficients:")

        for i in range(step + 1, len(remainder)):
            print(round(remainder[i], 2))

    print("\nFinal Quotient :")

    for i in range(quotient_degree + 1):
        power = quotient_degree - i
        print("Coefficient of x^" + str(power) + ":", round(remainder[i], 2))

    print("\nFinal Remainder :")

    remainder_start = quotient_degree + 1

    for i in range(remainder_start, len(remainder)):
        power = len(remainder) - i - 1
        print("Coefficient of x^" + str(power) + ":", round(remainder[i], 2))

polynomialdivisionstep()