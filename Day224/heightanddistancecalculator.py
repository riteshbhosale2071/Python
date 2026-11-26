import math

def heightanddistancecalculator():
    print("Height and Distance Calculator")
    print("1. Calculate Height")
    print("2. Calculate Distance")

    choice = input("Enter your choice (1-2): ")
    angle = float(input("Enter angle of elevation in degrees: "))

    if angle <= 0 or angle >= 90:
        print("Angle must be between 0 and 90 degrees.")
        return

    radian = math.radians(angle)

    if choice == "1":
        distance = float(input("Enter horizontal distance: "))
        if distance <= 0:
            print("Distance must be positive.")
            return
        height = distance * math.tan(radian)
        print("Height =", round(height, 2))

    elif choice == "2":
        height = float(input("Enter vertical height: "))
        if height <= 0:
            print("Height must be positive.")
            return
        distance = height / math.tan(radian)
        print("Horizontal Distance =", round(distance, 2))

    else:
        print("Invalid choice.")

heightanddistancecalculator()