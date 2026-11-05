import math

def heightmeasurementestimator():
    print("Height Measurement Estimator")
    print("1. Estimate height using shadow")
    print("2. Estimate height using distance and angle")

    choice = input("Enter your choice (1 or 2): ")

    try:
        if choice == "1":
            object_shadow = float(input("Enter object's shadow length: "))
            person_height = float(input("Enter person's height: "))
            person_shadow = float(input("Enter person's shadow length: "))

            if object_shadow <= 0 or person_height <= 0 or person_shadow <= 0:
                print("All measurements must be greater than zero.")
                return

            height = (object_shadow * person_height) / person_shadow
            print("Estimated height:", round(height, 2))

        elif choice == "2":
            distance = float(input("Enter horizontal distance from object: "))
            angle = float(input("Enter angle of elevation in degrees: "))
            observer_height = float(input("Enter observer's eye height: "))

            if distance <= 0 or observer_height < 0:
                print("Distance must be positive and eye height cannot be negative.")
                return

            if angle <= 0 or angle >= 90:
                print("Angle must be between 0 and 90 degrees.")
                return

            height = distance * math.tan(math.radians(angle)) + observer_height
            print("Estimated height:", round(height, 2))

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Please enter valid numeric measurements.")

heightmeasurementestimator()