def polynomialdivisiontable():
    print("Polynomial Division Table :")

    number_of_problems = int(input("Enter the number of polynomial divisions: "))

    print("\nDivision\tDividend Degree\tDivisor Degree\tQuotient Degree\tRemainder Status")

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

        for i in range(quotient_degree + 1):
            factor = remainder[i] / divisor[0]

            for j in range(divisor_degree + 1):
                remainder[i + j] -= factor * divisor[j]

        has_remainder = False

        for i in range(quotient_degree + 1, len(remainder)):
            if round(remainder[i], 2) != 0:
                has_remainder = True

        if has_remainder:
            remainder_status = "Non-zero"
        else:
            remainder_status = "Zero"

        print(
            str(problem) + "\t\t" +
            str(dividend_degree) + "\t\t" +
            str(divisor_degree) + "\t\t" +
            str(quotient_degree) + "\t\t" +
            remainder_status
        )

    print("\nPolynomial Division Table Completed :")

polynomialdivisiontable()