import math

def distancefromangleofdepression():
    print("Distance from Angle of Depression Calculator")

    try:
        height = float(input("Enter the height of the object: "))
        angle = float(input("Enter the angle of depression in degrees: "))

        if height <= 0:
            print("Height must be greater than zero.")
            return

        if angle <= 0 or angle >= 90:
            print("Angle must be between 0 and 90 degrees.")
            return

        distance = height / math.tan(math.radians(angle))

        print("Horizontal distance:", round(distance, 2))

    except ValueError:
        print("Please enter valid numeric values.")

distancefromangleofdepression()