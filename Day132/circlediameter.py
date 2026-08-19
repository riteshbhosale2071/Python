import math

def circlediameter():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Radius must be positive.")
        return

    diameter = 2 * radius

    print("Diameter of the Circle:", diameter)

circlediameter()