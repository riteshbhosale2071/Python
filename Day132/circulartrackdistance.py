import math

def circulartrackdistance():
    radius = float(input("Enter the radius of the circular track: "))
    laps = int(input("Enter the number of laps: "))

    if radius <= 0 or laps < 0:
        print("Enter a positive radius and non-negative number of laps.")
        return

    circumference = 2 * math.pi * radius
    total_distance = circumference * laps

    print("Distance for One Lap:", circumference)
    print("Total Distance:", total_distance)

circulartrackdistance()