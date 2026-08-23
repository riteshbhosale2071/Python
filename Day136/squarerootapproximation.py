import math

def squarerootapproximation():
    number = float(input("Enter a non-negative number: "))

    if number < 0:
        print("Square root is not defined for negative numbers.")
        return

    approximation = math.sqrt(number)

    print("Approximate Square Root:", approximation)

squarerootapproximation()