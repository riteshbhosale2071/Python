import math

def hypotenusefinder():
    base = float(input("Enter the base of the right triangle: "))
    height = float(input("Enter the height of the right triangle: "))

    if base <= 0 or height <= 0:
        print("Base and height must be positive.")
        return

    hypotenuse = math.sqrt(base ** 2 + height ** 2)

    print("Hypotenuse:", hypotenuse)

hypotenusefinder()