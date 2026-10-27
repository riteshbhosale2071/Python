import math

def pointdistancecalculator():
    print("POINT DISTANCE CALCULATOR :")

    print("\nChoose a calculation:")
    print("1. Distance between two 2D points")
    print("2. Distance between two 3D points")
    print("3. Distance from a point to the origin")
    print("4. Midpoint between two 2D points")
    print("5. Manhattan distance between two 2D points")

    choice = input("\nEnter your choice (1-5): ").strip()

    def get_coordinate(prompt):
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Enter a numeric coordinate.")
            return None

    if choice in ["1", "2", "4", "5"]:
        x1 = get_coordinate("Enter x1: ")
        if x1 is None:
            return

        y1 = get_coordinate("Enter y1: ")
        if y1 is None:
            return

        x2 = get_coordinate("Enter x2: ")
        if x2 is None:
            return

        y2 = get_coordinate("Enter y2: ")
        if y2 is None:
            return

        if choice == "1":
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            print("\nPoint A:", (x1, y1))
            print("Point B:", (x2, y2))
            print("Distance Formula: √((x2-x1)² + (y2-y1)²)")
            print("Distance:", round(distance, 4))

        elif choice == "2":
            z1 = get_coordinate("Enter z1: ")
            if z1 is None:
                return

            z2 = get_coordinate("Enter z2: ")
            if z2 is None:
                return

            distance = math.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2 +
                (z2 - z1) ** 2
            )

            print("\nPoint A:", (x1, y1, z1))
            print("Point B:", (x2, y2, z2))
            print("Distance Formula: √((x2-x1)² + (y2-y1)² + (z2-z1)²)")
            print("Distance:", round(distance, 4))

        elif choice == "4":
            midpoint_x = (x1 + x2) / 2
            midpoint_y = (y1 + y2) / 2

            print("\nMidpoint Formula: ((x1+x2)/2, (y1+y2)/2)")
            print("Midpoint:", (midpoint_x, midpoint_y))

        elif choice == "5":
            distance = abs(x2 - x1) + abs(y2 - y1)

            print("\nPoint A:", (x1, y1))
            print("Point B:", (x2, y2))
            print("Manhattan Distance:", distance)

    elif choice == "3":
        x = get_coordinate("Enter x coordinate: ")
        if x is None:
            return

        y = get_coordinate("Enter y coordinate: ")
        if y is None:
            return

        distance = math.sqrt(x ** 2 + y ** 2)

        print("\nPoint:", (x, y))
        print("Origin:", (0, 0))
        print("Distance Formula: √(x² + y²)")
        print("Distance from Origin:", round(distance, 4))

    else:
        print("Invalid choice! Select an option from 1 to 5.")
        return

    print("\nCalculation completed successfully.")

pointdistancecalculator()