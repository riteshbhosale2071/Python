import math

def repeatingdecimalfraction():
    numerator = int(input("Enter the repeating block (e.g. 3 for 0.333...): "))
    digits = len(str(abs(numerator)))

    if numerator < 0:
        numerator = abs(numerator)

    denominator = (10 ** digits) - 1

    gcd = math.gcd(numerator, denominator)
    numerator //= gcd
    denominator //= gcd

    if numerator == 0:
        print("Fraction: 0/1")
    else:
        print("Rational Fraction:", numerator, "/", denominator)

repeatingdecimalfraction()