import math

def circleareacalculator():
    radius = float(input("Enter the radius of the circle: "))

    if radius <= 0:
        print("Invalid radius. Radius must be positive.")
        return

    area = math.pi * radius ** 2

    print(f"Radius: {radius:.2f}")
    print(f"Circle Area: {area:.2f} square units")

circleareacalculator()