import math

def circlecircumference():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Radius must be positive.")
        return

    circumference = 2 * math.pi * radius

    print("Circumference:", circumference)

circlecircumference()