import math

def angleofdepressioncalculator():
    print("Angle of Depression Calculator")
    height = float(input("Enter vertical height: "))
    distance = float(input("Enter horizontal distance: "))

    if height < 0 or distance <= 0:
        print("Enter a non-negative height and positive distance.")
        return

    angle = math.degrees(math.atan(height / distance))

    print("Angle of Depression =", round(angle, 2), "degrees")

angleofdepressioncalculator()