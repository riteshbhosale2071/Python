from fractions import Fraction

def rationalnumordering():
    n = int(input("Enter the number of rational numbers: "))

    if n <= 0:
        print("Number of rational numbers must be positive.")
        return

    numbers = []

    for i in range(1, n + 1):
        print(f"\nRational Number {i}:")
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))

        if denominator == 0:
            print("Denominator cannot be zero.")
            return

        number = Fraction(numerator, denominator)
        numbers.append(number)

    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)

    print("\n--- Rational Number Ordering ---")

    print("\nAscending Order:")
    for number in ascending:
        print(number, "=", float(number))

    print("\nDescending Order:")
    for number in descending:
        print(number, "=", float(number))

rationalnumordering()