import math

def circleequationandmeasurement():
    print("Circle Equation and Measurement Calculator")
    print("1. Calculate using Radius")
    print("2. Calculate using Diameter")
    print("3. Calculate using Centre and Radius")
    print("4. Calculate Radius from Circumference")
    print("5. Calculate Radius from Area")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        h = 0
        k = 0

    elif choice == "2":
        diameter = float(input("Enter diameter: "))
        radius = diameter / 2
        h = 0
        k = 0

    elif choice == "3":
        h = float(input("Enter x-coordinate of centre: "))
        k = float(input("Enter y-coordinate of centre: "))
        radius = float(input("Enter radius: "))

    elif choice == "4":
        circumference = float(input("Enter circumference: "))
        radius = circumference / (2 * math.pi)
        h = 0
        k = 0

    elif choice == "5":
        area = float(input("Enter area: "))
        radius = math.sqrt(area / math.pi)
        h = 0
        k = 0

    else:
        print("Invalid choice.")
        return

    if radius <= 0:
        print("Radius must be positive.")
        return

    diameter = 2 * radius
    circumference = 2 * math.pi * radius
    area = math.pi * radius ** 2

    print("\nCircle Measurements:")
    print("Centre =", (h, k))
    print("Radius =", round(radius, 4))
    print("Diameter =", round(diameter, 4))
    print("Circumference =", round(circumference, 4))
    print("Area =", round(area, 4))

    print("\nStandard Circle Equation:")
    print(f"(x - ({h}))² + (y - ({k}))² = {round(radius ** 2, 4)}")

    print("\nGeneral Circle Equation:")
    print(f"x² + y² + ({-2*h})x + ({-2*k})y + ({h**2 + k**2 - radius**2}) = 0")

circleequationandmeasurement()