def quadrilateraltransformation():
    print("Quadrilateral Transformation Simulator :")

    x1 = float(input("Enter x-coordinate of point 1: "))
    y1 = float(input("Enter y-coordinate of point 1: "))

    x2 = float(input("Enter x-coordinate of point 2: "))
    y2 = float(input("Enter y-coordinate of point 2: "))

    x3 = float(input("Enter x-coordinate of point 3: "))
    y3 = float(input("Enter y-coordinate of point 3: "))

    x4 = float(input("Enter x-coordinate of point 4: "))
    y4 = float(input("Enter y-coordinate of point 4: "))

    print("\nChoose Transformation:")
    print("1. Translation")
    print("2. Reflection over X-axis")
    print("3. Reflection over Y-axis")
    print("4. Rotation 90 degrees clockwise")
    print("5. Rotation 90 degrees anticlockwise")

    choice = input("Enter your choice: ")

    if choice == "1":
        dx = float(input("Enter translation value in x-direction: "))
        dy = float(input("Enter translation value in y-direction: "))

        print("\nTransformed Coordinates:")
        print("Point 1:", x1 + dx, y1 + dy)
        print("Point 2:", x2 + dx, y2 + dy)
        print("Point 3:", x3 + dx, y3 + dy)
        print("Point 4:", x4 + dx, y4 + dy)

    elif choice == "2":
        print("\nReflected Coordinates over X-axis:")
        print("Point 1:", x1, -y1)
        print("Point 2:", x2, -y2)
        print("Point 3:", x3, -y3)
        print("Point 4:", x4, -y4)

    elif choice == "3":
        print("\nReflected Coordinates over Y-axis:")
        print("Point 1:", -x1, y1)
        print("Point 2:", -x2, y2)
        print("Point 3:", -x3, y3)
        print("Point 4:", -x4, y4)

    elif choice == "4":
        print("\nRotated Coordinates 90 Degrees Clockwise:")
        print("Point 1:", y1, -x1)
        print("Point 2:", y2, -x2)
        print("Point 3:", y3, -x3)
        print("Point 4:", y4, -x4)

    elif choice == "5":
        print("\nRotated Coordinates 90 Degrees Anticlockwise:")
        print("Point 1:", -y1, x1)
        print("Point 2:", -y2, x2)
        print("Point 3:", -y3, x3)
        print("Point 4:", -y4, x4)

    else:
        print("Invalid transformation choice.")

quadrilateraltransformation()