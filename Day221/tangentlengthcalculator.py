import math

def tangentlengthcalculator():
    print("Tangent Length Calculator")
    print("1. Find Tangent Length using Radius and Distance")
    print("2. Find Tangent Length using Coordinates")
    print("3. Find Tangent Length using Pythagorean Theorem")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        radius = float(input("Enter circle radius: "))
        distance = float(input("Enter distance from centre to external point: "))

        if radius <= 0 or distance <= radius:
            print("Invalid values: External point must be outside the circle.")
            return

        tangent = math.sqrt(distance ** 2 - radius ** 2)

    elif choice == "2":
        ox = float(input("Enter centre x-coordinate: "))
        oy = float(input("Enter centre y-coordinate: "))
        px = float(input("Enter external point x-coordinate: "))
        py = float(input("Enter external point y-coordinate: "))
        radius = float(input("Enter circle radius: "))

        distance = math.sqrt((px - ox) ** 2 + (py - oy) ** 2)

        if radius <= 0 or distance <= radius:
            print("Invalid values: External point must be outside the circle.")
            return

        tangent = math.sqrt(distance ** 2 - radius ** 2)

    elif choice == "3":
        hypotenuse = float(input("Enter distance from centre to external point: "))
        radius = float(input("Enter circle radius: "))

        if radius <= 0 or hypotenuse <= radius:
            print("Invalid values: Distance must be greater than radius.")
            return

        tangent = math.sqrt(hypotenuse ** 2 - radius ** 2)

    else:
        print("Invalid choice.")
        return

    print("\nTangent Length =", round(tangent, 4))
    print("Number of Tangents from External Point = 2")

tangentlengthcalculator()