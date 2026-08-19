import math

def wheelrotationcounter():
    distance = float(input("Enter the distance traveled: "))
    radius = float(input("Enter the wheel radius: "))

    if distance < 0 or radius <= 0:
        print("Enter a non-negative distance and positive radius.")
        return

    circumference = 2 * math.pi * radius
    rotations = distance / circumference

    print("Number of Wheel Rotations:", rotations)

wheelrotationcounter()