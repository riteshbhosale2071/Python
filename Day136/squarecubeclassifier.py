import math

def squarecubeclassifier():
    number = int(input("Enter a non-negative integer: "))

    if number < 0:
        print("Please enter a non-negative integer.")
        return

    square_root = math.isqrt(number)
    is_square = square_root ** 2 == number

    cube_root = round(number ** (1 / 3))
    is_cube = cube_root ** 3 == number

    if is_square and is_cube:
        print("The number is both a Perfect Square and a Perfect Cube.")
    elif is_square:
        print("The number is a Perfect Square.")
    elif is_cube:
        print("The number is a Perfect Cube.")
    else:
        print("The number is neither a Perfect Square nor a Perfect Cube.")

squarecubeclassifier()