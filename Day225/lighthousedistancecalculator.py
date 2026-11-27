import math

def lighthousedistancecalculator():
    print("Lighthouse Distance Calculator")
    print("1. Calculate horizontal distance from lighthouse")
    print("2. Calculate lighthouse height")

    choice = input("Enter your choice (1-2): ")
    angle = float(input("Enter angle of elevation or depression in degrees: "))

    if not 0 < angle < 90:
        print("Angle must be between 0 and 90 degrees.")
        return

    if choice == "1":
        height = float(input("Enter lighthouse height above sea level: "))
        observer_height = float(input("Enter observer's height above sea level: "))

        if height <= observer_height:
            print("Lighthouse height must be greater than observer height.")
            return

        distance = (height - observer_height) / math.tan(math.radians(angle))
        print("Horizontal Distance =", round(distance, 2), "units")

    elif choice == "2":
        distance = float(input("Enter horizontal distance: "))
        observer_height = float(input("Enter observer's height above sea level: "))

        if distance <= 0 or observer_height < 0:
            print("Invalid measurements.")
            return

        height = distance * math.tan(math.radians(angle)) + observer_height
        print("Lighthouse Height =", round(height, 2), "units")

    else:
        print("Invalid choice.")

lighthousedistancecalculator()