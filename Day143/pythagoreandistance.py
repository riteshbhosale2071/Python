import math

def pythagoreandistance():
    horizontal_distance = float(input("Enter horizontal distance: "))
    vertical_distance = float(input("Enter vertical distance: "))

    if horizontal_distance < 0 or vertical_distance < 0:
        print("Distances cannot be negative.")
        return

    distance = math.sqrt(
        horizontal_distance ** 2 + vertical_distance ** 2
    )

    print("Pythagorean Distance:", distance)

pythagoreandistance()