import math

def geometryrelationship():
    print("Geometry Relationship Solver :")
    print("1. Complementary Angles")
    print("2. Supplementary Angles")
    print("3. Linear Pair")
    print("4. Vertically Opposite Angles")
    print("5. Corresponding Angles")
    print("6. Alternate Interior Angles")
    print("7. Alternate Exterior Angles")
    print("8. Co-Interior Angles")

    choice = int(input("\nEnter relationship type: "))

    angle1 = float(input("Enter first angle: "))

    if not (0 < angle1 < 180):
        print("Angle must be between 0 and 180 degrees.")
        return

    if choice == 1:
        relationship = "Complementary Angles"
        target = 90
        unknown = 90 - angle1

    elif choice in (2, 3, 8):
        if choice == 2:
            relationship = "Supplementary Angles"
        elif choice == 3:
            relationship = "Linear Pair"
        else:
            relationship = "Co-Interior Angles"

        target = 180
        unknown = 180 - angle1

    elif choice in (4, 5, 6, 7):
        if choice == 4:
            relationship = "Vertically Opposite Angles"
        elif choice == 5:
            relationship = "Corresponding Angles"
        elif choice == 6:
            relationship = "Alternate Interior Angles"
        else:
            relationship = "Alternate Exterior Angles"

        target = angle1
        unknown = angle1

    else:
        print("Invalid choice.")
        return

    print("\nGeometry Relationship Solution :")
    print("Relationship:", relationship)
    print("Known Angle:", angle1, "degrees")
    print("Required Relationship Value:", target, "degrees")
    print("Unknown Angle:", unknown, "degrees")

    if unknown <= 0 or unknown >= 180:
        print("The given angle does not produce a valid second angle.")
    else:
        print("The unknown angle has been successfully calculated.")

geometryrelationship()