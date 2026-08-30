import math

def diagonalroom():
    length = float(input("Enter room length: "))
    width = float(input("Enter room width: "))
    height = float(input("Enter room height: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("Length, width, and height must be positive.")
        return

    diagonal = math.sqrt(
        length ** 2 + width ** 2 + height ** 2
    )

    print("Room Diagonal:", diagonal)

diagonalroom()