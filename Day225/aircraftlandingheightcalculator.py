import math

def aircraftlandingheightcalculator():
    print("Aircraft Landing Height Calculator")
    print("1. Calculate aircraft height")
    print("2. Calculate horizontal distance")

    choice = input("Enter your choice (1-2): ")
    angle = float(input("Enter angle of depression in degrees: "))

    if not 0 < angle < 90:
        print("Angle must be between 0 and 90 degrees.")
        return

    if choice == "1":
        distance = float(input("Enter horizontal distance from landing point: "))
        if distance <= 0:
            print("Distance must be positive.")
            return
        height = distance * math.tan(math.radians(angle))
        print("Aircraft Height =", round(height, 2), "units")

    elif choice == "2":
        height = float(input("Enter aircraft height above ground: "))
        if height <= 0:
            print("Height must be positive.")
            return
        distance = height / math.tan(math.radians(angle))
        print("Horizontal Distance =", round(distance, 2), "units")

    else:
        print("Invalid choice.")

aircraftlandingheightcalculator()