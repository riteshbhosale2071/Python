import math

def inscribedanglecalculator():
    print("Inscribed Angle Calculator")
    print("1. Find Inscribed Angle using Central Angle")
    print("2. Find Central Angle using Inscribed Angle")
    print("3. Find Inscribed Angle using Arc Length and Radius")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        central_angle = float(input("Enter central angle in degrees: "))

        if central_angle < 0 or central_angle > 360:
            print("Central angle must be between 0 and 360 degrees.")
            return

        inscribed_angle = central_angle / 2

    elif choice == "2":
        inscribed_angle = float(input("Enter inscribed angle in degrees: "))

        if inscribed_angle < 0 or inscribed_angle > 180:
            print("Inscribed angle must be between 0 and 180 degrees.")
            return

        central_angle = 2 * inscribed_angle

    elif choice == "3":
        radius = float(input("Enter circle radius: "))
        arc_length = float(input("Enter intercepted arc length: "))

        if radius <= 0 or arc_length < 0 or arc_length > 2 * math.pi * radius:
            print("Invalid radius or arc length.")
            return

        central_angle = math.degrees(arc_length / radius)
        inscribed_angle = central_angle / 2

    else:
        print("Invalid choice.")
        return

    print("\nInscribed Angle =", round(inscribed_angle, 4), "degrees")
    print("Central Angle =", round(central_angle, 4), "degrees")

    print("\nInscribed Angle Theorem:")
    print("The inscribed angle is half the measure of its intercepted arc.")

inscribedanglecalculator()