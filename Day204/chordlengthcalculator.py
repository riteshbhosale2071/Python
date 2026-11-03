import math

def chordlengthcalculator():
    radius = float(input("Enter the radius of the circle: "))
    angle = float(input("Enter the central angle in degrees: "))

    if radius <= 0:
        print("Invalid radius. Radius must be positive.")
        return

    if angle <= 0 or angle > 360:
        print("Invalid angle. Enter an angle between 0 and 360 degrees.")
        return

    chord_length = 2 * radius * math.sin(math.radians(angle / 2))

    print(f"Radius: {radius:.2f}")
    print(f"Central Angle: {angle:.2f} degrees")
    print(f"Chord Length: {chord_length:.2f} units")

chordlengthcalculator()