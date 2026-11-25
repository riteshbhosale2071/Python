def midpointfinder():
    print("Midpoint Finder")
    print("1. Find 2D Midpoint")
    print("2. Find 3D Midpoint")

    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))

        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2

        print("Midpoint =", (round(midpoint_x, 2), round(midpoint_y, 2)))

    elif choice == "2":
        x1 = float(input("Enter x1: "))
        y1 = float(input("Enter y1: "))
        z1 = float(input("Enter z1: "))
        x2 = float(input("Enter x2: "))
        y2 = float(input("Enter y2: "))
        z2 = float(input("Enter z2: "))

        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2
        midpoint_z = (z1 + z2) / 2

        print("3D Midpoint =", (
            round(midpoint_x, 2),
            round(midpoint_y, 2),
            round(midpoint_z, 2)
        ))

    else:
        print("Invalid choice.")

midpointfinder()