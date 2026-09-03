import math

def squarerootrationality():
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Square root of a negative number is not a real number.")
        return

    root = math.isqrt(number)

    if root * root == number:
        print("Square Root:", root)
        print("The square root is Rational.")
    else:
        print("Square Root:", math.sqrt(number))
        print("The square root is Irrational.")

squarerootrationality()