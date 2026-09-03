import math

def irrationalapproximation():
    number = int(input("Enter a positive integer: "))
    decimal_places = int(input("Enter number of decimal places: "))

    if number <= 0:
        print("Enter a positive integer.")
        return

    if decimal_places < 0:
        print("Decimal places cannot be negative.")
        return

    root = math.sqrt(number)
    rounded_root = round(root, decimal_places)

    perfect_square = math.isqrt(number) ** 2 == number

    print("\nIrrational Approximation :")
    print("Number:", number)
    print("Square Root:", rounded_root)

    if perfect_square:
        print("The square root is Rational.")
        print("Exact Square Root:", math.isqrt(number))
    else:
        print("The square root is Irrational.")
        print("Approximate Value:", rounded_root)

irrationalapproximation()