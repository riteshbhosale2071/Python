from fractions import Fraction

def rationalnumbermediants():
    numerator1 = int(input("Enter numerator of first fraction: "))
    denominator1 = int(input("Enter denominator of first fraction: "))

    numerator2 = int(input("Enter numerator of second fraction: "))
    denominator2 = int(input("Enter denominator of second fraction: "))

    terms = int(input("Enter number of mediants to generate: "))

    if denominator1 == 0 or denominator2 == 0:
        print("Denominator cannot be zero.")
        return

    if terms <= 0:
        print("Number of terms must be positive.")
        return

    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    if fraction1 >= fraction2:
        print("First fraction must be smaller than the second fraction.")
        return

    print("\nMediants :")

    left_num = fraction1.numerator
    left_den = fraction1.denominator

    right_num = fraction2.numerator
    right_den = fraction2.denominator

    for i in range(terms):
        mediant_num = left_num + right_num
        mediant_den = left_den + right_den

        mediant = Fraction(mediant_num, mediant_den)

        print(f"Medient {i + 1}: {mediant}")

        right_num = mediant.numerator
        right_den = mediant.denominator

rationalnumbermediants()