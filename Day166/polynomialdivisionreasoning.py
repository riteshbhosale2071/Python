def polynomialdivisionreasoning():
    print("Polynomial Division Reasoning Engine :")

    dividend_degree = int(input("Enter the degree of the dividend: "))
    divisor_degree = int(input("Enter the degree of the divisor: "))

    if divisor_degree > dividend_degree:
        print("Reason: The divisor degree is greater than the dividend degree.")
        print("Result: The quotient is zero and the remainder is the dividend.")
        return

    dividend = []
    divisor = []

    print("Enter dividend coefficients from highest degree to constant:")
    for i in range(dividend_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        dividend.append(coefficient)

    print("Enter divisor coefficients from highest degree to constant:")
    for i in range(divisor_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        divisor.append(coefficient)

    if divisor[0] == 0:
        print("Reason: The leading coefficient of the divisor is zero.")
        print("Result: Polynomial division cannot be performed.")
        return

    quotient_degree = dividend_degree - divisor_degree
    remainder = dividend[:]
    quotient = []

    print("\nReasoning Steps :")

    for i in range(quotient_degree + 1):
        factor = remainder[i] / divisor[0]
        quotient.append(round(factor, 2))

        print("\nStep", i + 1)
        print("Current coefficient:", round(remainder[i], 2))
        print("Division factor:", round(factor, 2))
        print("Reason: Divide the leading remainder coefficient by the leading divisor coefficient.")

        for j in range(divisor_degree + 1):
            remainder[i + j] -= factor * divisor[j]

        print("Reason: Multiply the divisor by the factor and subtract it from the remainder.")

    actual_remainder = []

    for i in range(quotient_degree + 1, len(remainder)):
        actual_remainder.append(round(remainder[i], 2))

    has_remainder = False

    for coefficient in actual_remainder:
        if coefficient != 0:
            has_remainder = True

    print("\nFinal Analysis :")
    print("Quotient Degree:", quotient_degree)
    print("Quotient Coefficients:", quotient)
    print("Remainder Coefficients:", actual_remainder)

    if has_remainder:
        print("Reason: At least one remainder coefficient is non-zero.")
        print("Conclusion: The dividend is not completely divisible by the divisor.")
    else:
        print("Reason: All remainder coefficients are zero.")
        print("Conclusion: The dividend is completely divisible by the divisor.")

    if quotient_degree == 0:
        print("Observation: The quotient is a constant polynomial.")
    elif quotient_degree == 1:
        print("Observation: The quotient is a linear polynomial.")
    elif quotient_degree == 2:
        print("Observation: The quotient is a quadratic polynomial.")
    else:
        print("Observation: The quotient has degree", quotient_degree)

polynomialdivisionreasoning()