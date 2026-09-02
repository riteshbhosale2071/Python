from fractions import Fraction

def rationalnumbergap():
    numerator1 = int(input("Enter numerator of first rational number: "))
    denominator1 = int(input("Enter denominator of first rational number: "))

    numerator2 = int(input("Enter numerator of second rational number: "))
    denominator2 = int(input("Enter denominator of second rational number: "))

    if denominator1 == 0 or denominator2 == 0:
        print("Denominator cannot be zero.")
        return

    number1 = Fraction(numerator1, denominator1)
    number2 = Fraction(numerator2, denominator2)

    gap = abs(number1 - number2)

    print("\nRational Number Gap Analysis :")
    print("First Rational Number:", number1)
    print("Second Rational Number:", number2)
    print("Gap Between Numbers:", gap)
    print("Decimal Gap:", float(gap))

    if gap == 0:
        print("Both rational numbers are equal.")
    elif gap < 1:
        print("The rational numbers are close together.")
    else:
        print("The rational numbers have a gap of 1 or more.")

rationalnumbergap()