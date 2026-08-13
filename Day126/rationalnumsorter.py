from fractions import Fraction

def rationalnumbersorter():
    count = int(input("Enter the number of rational numbers: "))
    numbers = []

    for i in range(count):
        numerator = int(input(f"Enter numerator of number {i + 1}: "))
        denominator = int(input(f"Enter denominator of number {i + 1}: "))

        if denominator == 0:
            print("Denominator cannot be zero.")
            return

        numbers.append(Fraction(numerator, denominator))

    numbers.sort()

    print("Rational Numbers in Ascending Order:")
    for number in numbers:
        print(number)

rationalnumbersorter()