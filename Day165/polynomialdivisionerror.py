def polynomialdivisionerror():
    print("Polynomial Division Error Detector :")

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
        print("Error: The leading coefficient of the divisor cannot be zero.")
        return

    if dividend_degree < divisor_degree:
        print("Error: Dividend degree must be greater than or equal to divisor degree.")
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

    reconstructed_dividend = []

    for i in range(dividend_degree + 1):
        reconstructed_dividend.append(0)

    for i in range(len(quotient)):
        for j in range(len(divisor)):
            reconstructed_dividend[i + j] += quotient[i] * divisor[j]

    for i in range(len(remainder_coefficients)):
        index = len(reconstructed_dividend) - len(remainder_coefficients) + i
        reconstructed_dividend[index] += remainder_coefficients[i]

    error_detected = False

    print("\n=== Error Detection Results ===")

    for i in range(len(dividend)):
        original_value = round(dividend[i], 2)
        reconstructed_value = round(reconstructed_dividend[i], 2)
        difference = round(abs(original_value - reconstructed_value), 2)

        print("Coefficient", i + 1)
        print("Original Value:", original_value)
        print("Reconstructed Value:", reconstructed_value)
        print("Difference:", difference)

        if difference > 0.01:
            error_detected = True

    if error_detected:
        print("\nError detected in polynomial division.")
        print("The reconstructed dividend does not match the original dividend.")
    else:
        print("\nNo error detected.")
        print("Polynomial division is verified successfully.")

polynomialdivisionerror()