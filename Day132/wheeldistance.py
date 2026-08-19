import math

def wheeldistance():
    radius = float(input("Enter the wheel radius: "))
    rotations = int(input("Enter the number of rotations: "))

    if radius <= 0 or rotations < 0:
        print("Enter a positive radius and non-negative rotations.")
        return

    circumference = 2 * math.pi * radius
    distance = circumference * rotations

    print("Distance traveled by the wheel:", distance)

wheeldistance()