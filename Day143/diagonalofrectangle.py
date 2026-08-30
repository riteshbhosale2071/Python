import math

def diagonalofrectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    if length <= 0 or width <= 0:
        print("Length and width must be positive.")
        return

    diagonal = math.sqrt(length ** 2 + width ** 2)

    print("Diagonal of Rectangle:", diagonal)

diagonalofrectangle()