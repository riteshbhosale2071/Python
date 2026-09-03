from fractions import Fraction

def fractionequalityvalidator():
    print("Enter the first fraction:")
    numerator1 = int(input("Enter numerator: "))
    denominator1 = int(input("Enter denominator: "))

    print("\nEnter the second fraction:")
    numerator2 = int(input("Enter numerator: "))
    denominator2 = int(input("Enter denominator: "))

    if denominator1 == 0 or denominator2 == 0:
        print("Denominator cannot be zero.")
        return

    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    print("\nFraction Equality Check :")
    print("First Fraction:", fraction1)
    print("Second Fraction:", fraction2)

    if fraction1 == fraction2:
        print("The fractions are Equal.")
    else:
        print("The fractions are Not Equal.")

fractionequalityvalidator()