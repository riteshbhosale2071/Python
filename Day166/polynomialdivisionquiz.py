def polynomialdivisionquiz():
    print("Polynomial Division Quiz Generator :")

    dividend_degree = int(input("Enter the degree of the dividend: "))
    divisor_degree = int(input("Enter the degree of the divisor: "))

    if divisor_degree > dividend_degree:
        print("The divisor degree cannot be greater than the dividend degree.")
        return

    dividend = []
    divisor = []

    print("\nEnter dividend coefficients from highest degree to constant:")
    for i in range(dividend_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        dividend.append(coefficient)

    print("\nEnter divisor coefficients from highest degree to constant:")
    for i in range(divisor_degree + 1):
        coefficient = float(input("Enter coefficient " + str(i + 1) + ": "))
        divisor.append(coefficient)

    if divisor[0] == 0:
        print("The leading coefficient of the divisor cannot be zero.")
        return

    quotient_degree = dividend_degree - divisor_degree
    remainder = dividend[:]
    quotient = []

    for i in range(quotient_degree + 1):
        factor = remainder[i] / divisor[0]
        quotient.append(round(factor, 2))

        for j in range(divisor_degree + 1):
            remainder[i + j] -= factor * divisor[j]

    print("\nPolynomial Division Quiz :")

    print("\nQuestion 1:")
    print("What is the degree of the quotient?")
    answer1 = int(input("Your answer: "))

    if answer1 == quotient_degree:
        print("Correct!")
    else:
        print("Incorrect. Correct answer:", quotient_degree)

    print("\nQuestion 2:")
    print("What is the leading coefficient of the quotient?")
    answer2 = float(input("Your answer: "))

    if round(answer2, 2) == quotient[0]:
        print("Correct!")
    else:
        print("Incorrect. Correct answer:", quotient[0])

    remainder_start = quotient_degree + 1
    actual_remainder = []

    for i in range(remainder_start, len(remainder)):
        actual_remainder.append(round(remainder[i], 2))

    print("\nQuestion 3:")
    print("Is the remainder zero?")
    answer3 = input("Enter yes or no: ").lower()

    remainder_is_zero = True

    for coefficient in actual_remainder:
        if coefficient != 0:
            remainder_is_zero = False

    if (answer3 == "yes" and remainder_is_zero) or (answer3 == "no" and not remainder_is_zero):
        print("Correct!")
    else:
        if remainder_is_zero:
            print("Incorrect. Correct answer: yes")
        else:
            print("Incorrect. Correct answer: no")

    print("\nQuiz Completed :")
    print("Quotient Degree:", quotient_degree)
    print("Quotient Coefficients:", quotient)
    print("Remainder Coefficients:", actual_remainder)

polynomialdivisionquiz()