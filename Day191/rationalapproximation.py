def rationalapproximation():
    print("Rational Approximation :")

    try:
        number = float(input("Enter a decimal number: "))
        max_denominator = int(input("Enter the maximum denominator: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        return

    if max_denominator <= 0:
        print("Maximum denominator must be greater than zero.")
        return

    best_numerator = 0
    best_denominator = 1
    smallest_error = float("inf")

    approximations = []

    for denominator in range(1, max_denominator + 1):
        numerator = round(number * denominator)
        approximation = numerator / denominator
        error = abs(number - approximation)

        approximations.append(
            (numerator, denominator, approximation, error)
        )

        if error < smallest_error:
            smallest_error = error
            best_numerator = numerator
            best_denominator = denominator

    a = abs(best_numerator)
    b = best_denominator

    while b != 0:
        remainder = a % b
        a = b
        b = remainder

    gcd = a

    if gcd != 0:
        best_numerator //= gcd
        best_denominator //= gcd

    print("\nApproximation Results :")
    print("Original Number:", number)
    print("Best Rational Approximation:",
          str(best_numerator) + "/" + str(best_denominator))
    print("Decimal Approximation:",
          round(best_numerator / best_denominator, 10))
    print("Absolute Error:", round(smallest_error, 10))

    print("\nRational Approximations :")
    print("{:<15} {:<15} {:<20} {:<15}".format(
        "Numerator", "Denominator", "Approximation", "Error"
    ))
    print("-" * 65)

    for numerator, denominator, approximation, error in approximations:
        print("{:<15} {:<15} {:<20.10f} {:<15.10f}".format(
            numerator, denominator, approximation, error
        ))

    print("\nAccuracy Analysis :")

    if smallest_error == 0:
        print("The input number has an exact rational representation within the search.")
    elif smallest_error < 0.001:
        print("The best approximation is highly accurate.")
    elif smallest_error < 0.01:
        print("The best approximation is reasonably accurate.")
    else:
        print("Increase the maximum denominator for potentially better accuracy.")

    print("Maximum Denominator Checked:", max_denominator)

rationalapproximation()