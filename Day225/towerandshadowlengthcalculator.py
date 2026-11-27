import math

def towerandshadowlengthcalculator():
    print("Tower and Shadow Length Calculator")
    print("1. Calculate tower height")
    print("2. Calculate shadow length")

    choice = input("Enter your choice (1-2): ")
    angle = float(input("Enter angle of elevation in degrees: "))

    if not 0 < angle < 90:
        print("Angle must be between 0 and 90 degrees.")
        return

    if choice == "1":
        shadow = float(input("Enter shadow length: "))
        if shadow <= 0:
            print("Shadow length must be positive.")
            return
        height = shadow * math.tan(math.radians(angle))
        print("Tower Height =", round(height, 2), "units")

    elif choice == "2":
        height = float(input("Enter tower height: "))
        if height <= 0:
            print("Tower height must be positive.")
            return
        shadow = height / math.tan(math.radians(angle))
        print("Shadow Length =", round(shadow, 2), "units")

    else:
        print("Invalid choice.")

towerandshadowlengthcalculator()