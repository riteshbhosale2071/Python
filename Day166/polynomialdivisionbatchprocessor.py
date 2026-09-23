def polynomialdivisionbatchprocessor():
    print("Polynomial Division Batch Processor :")

    number_of_problems = int(input("Enter the number of polynomial divisions: "))

    for problem in range(1, number_of_problems + 1):
        print("\nDivision", problem, ":")

        dividend_degree = int(input("Enter the degree of the dividend: "))
        divisor_degree = int(input("Enter the degree of the divisor: "))

        if divisor_degree > dividend_degree:
            print("The divisor degree cannot be greater than the dividend degree.")
            continue

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
            print("The leading coefficient of the divisor cannot be zero.")
            continue

        quotient_degree = dividend_degree - divisor_degree
        remainder = dividend[:]
        quotient = []

        for i in range(quotient_degree + 1):
            factor = remainder[i] / divisor[0]
            quotient.append(round(factor, 2))

            for j in range(divisor_degree + 1):
                remainder[i + j] -= factor * divisor[j]

        actual_remainder = []

        for i in range(quotient_degree + 1, len(remainder)):
            actual_remainder.append(round(remainder[i], 2))

        print("\nQuotient Coefficients:", quotient)
        print("Remainder Coefficients:", actual_remainder)

        has_remainder = False

        for coefficient in actual_remainder:
            if coefficient != 0:
                has_remainder = True

        if has_remainder:
            print("Division Status: Non-zero remainder")
        else:
            print("Division Status: Completely divisible")

    print("\nBatch Processing Completed !!!")

polynomialdivisionbatchprocessor()