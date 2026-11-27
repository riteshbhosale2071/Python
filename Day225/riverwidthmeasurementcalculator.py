import math

def riverwidthmeasurementcalculator():
    print("River Width Measurement Calculator")
    print("1. Calculate river width using angle of elevation")
    print("2. Calculate river width using tangent ratio")

    choice = input("Enter your choice (1-2): ")

    if choice in ("1", "2"):
        angle = float(input("Enter measured angle in degrees: "))

        if not 0 < angle < 90:
            print("Angle must be between 0 and 90 degrees.")
            return

        distance = float(input("Enter distance from observation point to reference point: "))

        if distance <= 0:
            print("Distance must be positive.")
            return

        width = distance * math.tan(math.radians(angle))
        print("Estimated River Width =", round(width, 2), "units")

    else:
        print("Invalid choice.")

riverwidthmeasurementcalculator()