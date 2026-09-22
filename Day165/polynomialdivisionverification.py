def polynomialdivisionverification():
    print("Polynomial Division Verification :")

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
        print("The degree of the dividend must be greater than or equal to the divisor.")
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

    remainder_start = quotient_degree + 1
    remainder_coefficients = []

    for i in range(remainder_start, len(remainder)):
        remainder_coefficients.append(remainder[i])

    product = []

    for i in range(dividend_degree + 1):
        product.append(0)

    for i in range(len(quotient)):
        for j in range(len(divisor)):
            product[i + j] += quotient[i] * divisor[j]

    reconstructed_dividend = []

    for i in range(len(product)):
        reconstructed_dividend.append(product[i])

    for i in range(len(remainder_coefficients)):
        index = len(reconstructed_dividend) - len(remainder_coefficients) + i
        reconstructed_dividend[index] += remainder_coefficients[i]

    print("\nQuotient Coefficients:")
    for coefficient in quotient:
        print(round(coefficient, 2))

    print("\nRemainder Coefficients:")
    for coefficient in remainder_coefficients:
        print(round(coefficient, 2))

    print("\nVerification Results:")

    verified = True

    if len(dividend) != len(reconstructed_dividend):
        verified = False
    else:
        for i in range(len(dividend)):
            original_value = round(dividend[i], 2)
            reconstructed_value = round(reconstructed_dividend[i], 2)

            print("Original:", original_value, "Reconstructed:", reconstructed_value)

            if abs(original_value - reconstructed_value) > 0.01:
                verified = False

    if verified:
        print("Verification successful.")
        print("Dividend = Divisor × Quotient + Remainder")
    else:
        print("Verification failed.")

polynomialdivisionverification()