from fractions import Fraction

def rationalnumoperationpattern():
    n = int(input("Enter the number of rational numbers: "))

    if n < 3:
        print("Enter at least 3 rational numbers.")
        return

    numbers = []

    for i in range(1, n + 1):
        print(f"\nRational Number {i}:")
        numerator = int(input("Enter numerator: "))
        denominator = int(input("Enter denominator: "))

        if denominator == 0:
            print("Denominator cannot be zero.")
            return

        numbers.append(Fraction(numerator, denominator))

    differences = []
    ratios = []

    for i in range(1, n):
        differences.append(numbers[i] - numbers[i - 1])

        if numbers[i - 1] != 0:
            ratios.append(numbers[i] / numbers[i - 1])
        else:
            ratios.append(None)

    print("\nOperation Pattern Analysis :")

    if all(difference == differences[0] for difference in differences):
        print("Pattern Detected: Constant Difference")
        print("Common Difference:", differences[0])

    elif all(ratio is not None and ratio == ratios[0] for ratio in ratios):
        print("Pattern Detected: Constant Ratio")
        print("Common Ratio:", ratios[0])

    else:
        print("No constant operation pattern detected.")

    print("\nSequence:")
    for number in numbers:
        print(number, "=", float(number))

rationalnumoperationpattern()