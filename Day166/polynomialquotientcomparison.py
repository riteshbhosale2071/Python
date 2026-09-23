def polynomialquotientcomparison():
    print("Polynomial Quotient Comparison :")

    degree1 = int(input("Enter the degree of the first dividend: "))
    divisor_degree1 = int(input("Enter the degree of the first divisor: "))

    if divisor_degree1 > degree1:
        print("The divisor degree cannot be greater than the dividend degree.")
        return

    dividend1 = []
    divisor1 = []

    print("Enter first dividend coefficients from highest degree to constant:")
    for i in range(degree1 + 1):
        dividend1.append(float(input("Enter coefficient " + str(i + 1) + ": ")))

    print("Enter first divisor coefficients from highest degree to constant:")
    for i in range(divisor_degree1 + 1):
        divisor1.append(float(input("Enter coefficient " + str(i + 1) + ": ")))

    if divisor1[0] == 0:
        print("The leading coefficient of the first divisor cannot be zero.")
        return

    degree2 = int(input("\nEnter the degree of the second dividend: "))
    divisor_degree2 = int(input("Enter the degree of the second divisor: "))

    if divisor_degree2 > degree2:
        print("The divisor degree cannot be greater than the dividend degree.")
        return

    dividend2 = []
    divisor2 = []

    print("Enter second dividend coefficients from highest degree to constant:")
    for i in range(degree2 + 1):
        dividend2.append(float(input("Enter coefficient " + str(i + 1) + ": ")))

    print("Enter second divisor coefficients from highest degree to constant:")
    for i in range(divisor_degree2 + 1):
        divisor2.append(float(input("Enter coefficient " + str(i + 1) + ": ")))

    if divisor2[0] == 0:
        print("The leading coefficient of the second divisor cannot be zero.")
        return

    quotient_degree1 = degree1 - divisor_degree1
    quotient_degree2 = degree2 - divisor_degree2

    remainder1 = dividend1[:]
    remainder2 = dividend2[:]

    quotient1 = []
    quotient2 = []

    for i in range(quotient_degree1 + 1):
        factor = remainder1[i] / divisor1[0]
        quotient1.append(round(factor, 2))

        for j in range(divisor_degree1 + 1):
            remainder1[i + j] -= factor * divisor1[j]

    for i in range(quotient_degree2 + 1):
        factor = remainder2[i] / divisor2[0]
        quotient2.append(round(factor, 2))

        for j in range(divisor_degree2 + 1):
            remainder2[i + j] -= factor * divisor2[j]

    print("\nQuotient Comparison :")
    print("First Quotient Degree:", quotient_degree1)
    print("First Quotient Coefficients:", quotient1)

    print("\nSecond Quotient Degree:", quotient_degree2)
    print("Second Quotient Coefficients:", quotient2)

    if quotient_degree1 > quotient_degree2:
        print("\nThe first quotient has a higher degree.")
    elif quotient_degree2 > quotient_degree1:
        print("\nThe second quotient has a higher degree.")
    else:
        print("\nBoth quotients have the same degree.")

    if quotient1 == quotient2:
        print("Both quotients are equal.")
    else:
        print("The quotients are different.")

polynomialquotientcomparison()