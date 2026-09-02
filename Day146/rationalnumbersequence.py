from fractions import Fraction

def rationalnumbersequence():
    numerator = int(input("Enter starting numerator: "))
    denominator = int(input("Enter denominator: "))
    step = int(input("Enter numerator step: "))
    terms = int(input("Enter number of terms: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    if terms <= 0:
        print("Number of terms must be positive.")
        return

    print("\n--- Rational Number Sequence ---")

    for i in range(terms):
        current_numerator = numerator + (i * step)
        fraction = Fraction(current_numerator, denominator)

        print(
            f"Term {i + 1}: "
            f"{current_numerator}/{denominator} = {float(fraction)}"
        )

rationalnumbersequence()