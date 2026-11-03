import math

def circumferencecalculator():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Invalid radius. Radius must be positive.")
        return

    circumference = 2 * math.pi * radius
    diameter = 2 * radius

    print(f"Radius: {radius:.2f}")
    print(f"Diameter: {diameter:.2f}")
    print(f"Circumference: {circumference:.2f} units")

circumferencecalculator()