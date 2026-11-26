import math

def angleofelevationcalculator():
    print("Angle of Elevation Calculator")
    height = float(input("Enter vertical height: "))
    distance = float(input("Enter horizontal distance: "))

    if height < 0 or distance <= 0:
        print("Enter a non-negative height and positive distance.")
        return

    angle = math.degrees(math.atan(height / distance))

    print("Angle of Elevation =", round(angle, 2), "degrees")

angleofelevationcalculator()