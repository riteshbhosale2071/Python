import math

def buildingheightmeasurement():
    print("Building Height Measurement System")
    print("1. Calculate height using angle of elevation")
    print("2. Calculate height using angle and distance from building")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        distance = float(input("Enter horizontal distance from building: "))
        angle = float(input("Enter angle of elevation in degrees: "))
        observer_height = float(input("Enter observer's height from ground: "))

        if distance <= 0 or observer_height < 0 or not 0 < angle < 90:
            print("Invalid measurements.")
            return

        height = distance * math.tan(math.radians(angle)) + observer_height
        print("Building Height =", round(height, 2), "units")

    elif choice == "2":
        distance = float(input("Enter horizontal distance from building: "))
        angle = float(input("Enter angle of elevation in degrees: "))

        if distance <= 0 or not 0 < angle < 90:
            print("Invalid measurements.")
            return

        height = distance * math.tan(math.radians(angle))
        print("Building Height =", round(height, 2), "units")

    else:
        print("Invalid choice.")

buildingheightmeasurement()