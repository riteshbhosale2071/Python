import math

def circleradiusfinder():
    print("Circle Radius Finder")
    print("1. Find Radius using Diameter")
    print("2. Find Radius using Circumference")
    print("3. Find Radius using Area")
    print("4. Find Radius using Chord and Perpendicular Distance")
    print("5. Find Radius using Chord and Central Angle")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        diameter = float(input("Enter diameter: "))
        radius = diameter / 2

    elif choice == "2":
        circumference = float(input("Enter circumference: "))
        if circumference <= 0:
            print("Circumference must be positive.")
            return
        radius = circumference / (2 * math.pi)

    elif choice == "3":
        area = float(input("Enter area: "))
        if area <= 0:
            print("Area must be positive.")
            return
        radius = math.sqrt(area / math.pi)

    elif choice == "4":
        chord = float(input("Enter chord length: "))
        distance = float(input("Enter perpendicular distance from centre to chord: "))
        if chord <= 0 or distance < 0:
            print("Invalid measurements.")
            return
        radius = math.sqrt((chord / 2) ** 2 + distance ** 2)

    elif choice == "5":
        chord = float(input("Enter chord length: "))
        angle = float(input("Enter central angle in degrees: "))
        if chord <= 0 or angle <= 0 or angle > 180:
            print("Enter a positive chord and an angle between 0 and 180.")
            return
        radius = chord / (2 * math.sin(math.radians(angle / 2)))

    else:
        print("Invalid choice.")
        return

    if radius <= 0:
        print("Radius must be positive.")
        return

    print("\nCircle Radius =", round(radius, 4))
    print("Diameter =", round(2 * radius, 4))
    print("Circumference =", round(2 * math.pi * radius, 4))
    print("Area =", round(math.pi * radius ** 2, 4))

circleradiusfinder()