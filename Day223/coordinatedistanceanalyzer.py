import math

def coordinatedistanceanalyzer():
    print("Coordinate Distance Analyzer")
    print("1. Analyze 2D Coordinates")
    print("2. Analyze 3D Coordinates")
    print("3. Find Distance and Midpoint")
    print("4. Find Manhattan Distance")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        distance = math.hypot(x2 - x1, y2 - y1)
        print("Distance =", round(distance, 2))
        print("Horizontal Difference =", round(abs(x2 - x1), 2))
        print("Vertical Difference =", round(abs(y2 - y1), 2))

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

        distance = math.hypot(x2 - x1, y2 - y1)
        midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

        print("Distance =", round(distance, 2))
        print("Midpoint =", (round(midpoint[0], 2), round(midpoint[1], 2)))

    elif choice == "4":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        distance = abs(x2 - x1) + abs(y2 - y1)
        print("Manhattan Distance =", round(distance, 2))

    else:
        print("Invalid choice.")

coordinatedistanceanalyzer()