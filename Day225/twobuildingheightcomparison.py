import math

def twobuildingheightcomparison():
    print("Two Building Height Comparison")
    print("1. Compare heights using shadow lengths")
    print("2. Compare heights using angles of elevation")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        shadow1 = float(input("Enter first building's shadow length: "))
        shadow2 = float(input("Enter second building's shadow length: "))
        angle = float(input("Enter common angle of elevation in degrees: "))

        if shadow1 <= 0 or shadow2 <= 0 or not 0 < angle < 90:
            print("Invalid measurements.")
            return

        height1 = shadow1 * math.tan(math.radians(angle))
        height2 = shadow2 * math.tan(math.radians(angle))

    elif choice == "2":
        distance1 = float(input("Enter distance from first building: "))
        angle1 = float(input("Enter angle of elevation for first building: "))
        distance2 = float(input("Enter distance from second building: "))
        angle2 = float(input("Enter angle of elevation for second building: "))

        if distance1 <= 0 or distance2 <= 0 or not (0 < angle1 < 90 and 0 < angle2 < 90):
            print("Invalid measurements.")
            return

        height1 = distance1 * math.tan(math.radians(angle1))
        height2 = distance2 * math.tan(math.radians(angle2))

    else:
        print("Invalid choice.")
        return

    print("First Building Height =", round(height1, 2), "units")
    print("Second Building Height =", round(height2, 2), "units")

    if math.isclose(height1, height2, rel_tol=1e-9):
        print("Both buildings have equal heights.")
    elif height1 > height2:
        print("First building is taller by", round(height1 - height2, 2), "units.")
    else:
        print("Second building is taller by", round(height2 - height1, 2), "units.")

twobuildingheightcomparison()