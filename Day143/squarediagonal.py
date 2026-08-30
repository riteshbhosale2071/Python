import math

def squarediagonal():
    side = float(input("Enter the side of the square: "))

    if side <= 0:
        print("Side must be positive.")
        return

    diagonal = side * math.sqrt(2)

    print("Diagonal of Square:", diagonal)

squarediagonal()