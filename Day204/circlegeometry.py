import math

def circlegeometry():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Invalid radius. Radius must be positive.")
        return

    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    print("\nCircle Geometry Report :")
    print(f"Radius: {radius:.2f} units")
    print(f"Diameter: {diameter:.2f} units")
    print(f"Circumference: {circumference:.2f} units")
    print(f"Area: {area:.2f} square units")
    print(f"Radius Squared: {radius ** 2:.2f}")
    print(f"Circle Equation: x^2 + y^2 = {radius ** 2:.2f}")

circlegeometry()