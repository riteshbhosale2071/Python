from fractions import Fraction

def rationalnumberdistance():
    n1 = int(input("Enter numerator of first rational number: "))
    d1 = int(input("Enter denominator of first rational number: "))

    n2 = int(input("Enter numerator of second rational number: "))
    d2 = int(input("Enter denominator of second rational number: "))

    if d1 == 0 or d2 == 0:
        print("Denominator cannot be zero.")
        return

    number1 = Fraction(n1, d1)
    number2 = Fraction(n2, d2)

    distance = abs(number1 - number2)

    print("\nRational Number Distance :")
    print("First Rational Number:", number1)
    print("Second Rational Number:", number2)
    print("Distance:", distance)
    print("Decimal Distance:", float(distance))

rationalnumberdistance()