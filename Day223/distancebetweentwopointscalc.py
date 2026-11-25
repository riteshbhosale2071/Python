import math

def distancebetweentwopointscalc():
    print("Distance Between Two Points Calculator")
    print("1. Calculate 2D Distance")
    print("2. Calculate 3D Distance")
    print("3. Find Midpoint Between Two Points")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print("Distance =", round(distance, 2))

    elif choice == "2":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        print("3D Distance =", round(distance, 2))

    elif choice == "3":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2

        print("Midpoint =", (round(midpoint_x, 2), round(midpoint_y, 2)))

    else:
        print("Invalid choice.")

distancebetweentwopointscalc()