import math

def rationalnumterminatingdecimal():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    gcd = math.gcd(abs(numerator), abs(denominator))
    denominator = abs(denominator) // gcd

    while denominator % 2 == 0:
        denominator //= 2

    while denominator % 5 == 0:
        denominator //= 5

    if denominator == 1:
        print("The rational number has a Terminating Decimal.")
    else:
        print("The rational number has a Non-Terminating Repeating Decimal.")

rationalnumterminatingdecimal()