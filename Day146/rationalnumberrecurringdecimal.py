import math

def rationalnumberrecurringdecimal():
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    if denominator == 0:
        print("Denominator cannot be zero.")
        return

    if numerator == 0:
        print("The decimal representation is Terminating (0).")
        return

    gcd = math.gcd(abs(numerator), abs(denominator))
    denominator = abs(denominator) // gcd

    temp = denominator

    while temp % 2 == 0:
        temp //= 2

    while temp % 5 == 0:
        temp //= 5

    if temp == 1:
        print("The decimal is Terminating.")
    else:
        print("The decimal is Non-Terminating and Repeating.")

rationalnumberrecurringdecimal()