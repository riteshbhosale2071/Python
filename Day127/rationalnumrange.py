from fractions import Fraction

def rationalnumrange():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    number = Fraction(numerator, denominator)

    lower = float(input("Enter lower limit: "))
    upper = float(input("Enter upper limit: "))

    if lower > upper:
        lower, upper = upper, lower

    if lower <= number <= upper:
        print("The rational number lies within the range.")
    else:
        print("The rational number lies outside the range.")

rationalnumrange()