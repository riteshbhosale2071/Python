import math

def cuberootintegerchecker():
    print("Cube Root Integer Checker :")

    number = int(input("Enter an integer: "))

    root = round(abs(number) ** (1 / 3))

    while (root + 1) ** 3 <= abs(number):
        root += 1

    while root ** 3 > abs(number):
        root -= 1

    if number < 0:
        cube_root = -root
    else:
        cube_root = root

    print("\nCube Root Analysis :")
    print("Number:", number)
    print("Integer Cube Root:", cube_root)

    if cube_root ** 3 == number:
        print("Result: The number is a perfect cube.")
        print(f"{number} = {cube_root}³")
    else:
        print("Result: The number is not a perfect cube.")
        print("Its cube root is not an integer.")

cuberootintegerchecker()