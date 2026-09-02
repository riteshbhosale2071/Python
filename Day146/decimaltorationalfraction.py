import math

def decimaltorationalfraction():
    decimal = float(input("Enter a decimal number: "))

    decimal_text = str(decimal)

    if "." in decimal_text:
        decimal_places = len(decimal_text.split(".")[1])
        denominator = 10 ** decimal_places
        numerator = round(decimal * denominator)
    else:
        numerator = int(decimal)
        denominator = 1

    gcd = math.gcd(abs(numerator), denominator)
    numerator //= gcd
    denominator //= gcd

    print("Rational Fraction:", numerator, "/", denominator)

decimaltorationalfraction()