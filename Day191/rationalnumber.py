def rationalnumber():
    print("Rational Number Generator :")

    try:
        n = int(input("Enter the number of rational numbers to generate: "))
    except ValueError:
        print("Invalid input! Enter a positive integer.")
        return

    if n <= 0:
        print("Number of rational numbers must be greater than zero.")
        return

    rational_numbers = []

    for i in range(n):
        print("\nRational Number", i + 1)

        try:
            numerator = int(input("Enter numerator: "))
            denominator = int(input("Enter denominator: "))
        except ValueError:
            print("Invalid input! Numerator and denominator must be integers.")
            return

        if denominator == 0:
            print("Denominator cannot be zero. Try again.")
            continue

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        a = abs(numerator)
        b = denominator

        while b != 0:
            remainder = a % b
            a = b
            b = remainder

        gcd = a

        if gcd != 0:
            numerator //= gcd
            denominator //= gcd
        else:
            denominator = 1

        rational_numbers.append((numerator, denominator))

    print("\nGenerated Rational Numbers :")

    for i, fraction in enumerate(rational_numbers, start=1):
        numerator, denominator = fraction

        if denominator == 1:
            print(str(i) + ".", numerator)
        else:
            print(str(i) + ".", str(numerator) + "/" + str(denominator))

    print("\nTotal Rational Numbers Generated:", len(rational_numbers))

    unique_numbers = []

    for fraction in rational_numbers:
        if fraction not in unique_numbers:
            unique_numbers.append(fraction)

    print("Distinct Rational Numbers:", len(unique_numbers))

    print("\nDecimal Representations :")

    for numerator, denominator in rational_numbers:
        decimal_value = numerator / denominator
        print(
            str(numerator) + "/" + str(denominator),
            "=",
            round(decimal_value, 6)
        )

rationalnumber()