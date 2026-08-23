import math

def perfectsquarechecker():
    number = int(input("Enter a number: "))

    if number < 0:
        print("Negative numbers are not perfect squares.")
        return

    square_root = math.isqrt(number)

    if square_root ** 2 == number:
        print("The number is a Perfect Square.")
    else:
        print("The number is not a Perfect Square.")

perfectsquarechecker()