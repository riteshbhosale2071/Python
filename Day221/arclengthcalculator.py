import math

def arclengthcalculator():
    print("Arc Length Calculator")
    print("1. Using Radius and Central Angle")
    print("2. Using Radius and Angle in Radians")
    print("3. Using Circumference and Central Angle")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        angle = float(input("Enter central angle in degrees: "))

        if radius <= 0 or angle < 0 or angle > 360:
            print("Invalid radius or angle.")
            return

        arc_length = (angle / 360) * 2 * math.pi * radius

    elif choice == "2":
        radius = float(input("Enter radius: "))
        angle = float(input("Enter central angle in radians: "))

        if radius <= 0 or angle < 0 or angle > 2 * math.pi:
            print("Invalid radius or angle.")
            return

        arc_length = radius * angle

    elif choice == "3":
        circumference = float(input("Enter circumference: "))
        angle = float(input("Enter central angle in degrees: "))

        if circumference <= 0 or angle < 0 or angle > 360:
            print("Invalid circumference or angle.")
            return

        arc_length = (angle / 360) * circumference

    else:
        print("Invalid choice.")
        return

    print("\nArc Length =", round(arc_length, 4))

arclengthcalculator()