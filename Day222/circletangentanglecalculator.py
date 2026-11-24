import math

def circletangentanglecalculator():
    print("Circle Tangent Angle Calculator")
    print("1. Find Angle Between Tangent and Radius")
    print("2. Find Angle Between Two Tangents")
    print("3. Find Central Angle Between Tangent Points")
    print("4. Verify Tangent-Radius Perpendicularity")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        angle = 90
        print("Angle between tangent and radius =", angle, "degrees")

    elif choice == "2":
        central = float(input("Enter central angle between tangent points: "))

        if not 0 < central < 360:
            print("Central angle must be between 0 and 360 degrees.")
            return

        tangent_angle = 180 - central
        print("Angle Between Two Tangents =", round(tangent_angle, 2), "degrees")

    elif choice == "3":
        tangent_angle = float(input("Enter angle between two tangents: "))

        if not 0 < tangent_angle < 180:
            print("Tangent angle must be between 0 and 180 degrees.")
            return

        central = 180 - tangent_angle
        print("Central Angle =", round(central, 2), "degrees")

    elif choice == "4":
        angle = float(input("Enter measured angle between radius and tangent: "))

        if not 0 <= angle <= 180:
            print("Invalid angle.")
            return

        if math.isclose(angle, 90, abs_tol=1e-9):
            print("Verified: Radius is perpendicular to the tangent.")
        else:
            print("Not verified: Radius and tangent are not perpendicular.")

    else:
        print("Invalid choice.")

circletangentanglecalculator()