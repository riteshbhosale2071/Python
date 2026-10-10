def polygonpartitionplanner():
    print("Polygon Partition Planner :")

    sides = int(input("Enter number of polygon sides: "))

    if sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    print("\n1. Triangles formed from one vertex")
    print("2. Minimum triangles required")
    print("3. Total interior angles")
    print("4. Interior angle sum of each regular polygon")

    choice = int(input("Select an option: "))

    if choice == 1:
        triangles = sides - 2
        diagonals = sides - 3

        print("Triangles formed:", triangles)
        print("Diagonals drawn from one vertex:", diagonals)

    elif choice == 2:
        triangles = sides - 2
        print("Minimum triangles required:", triangles)

    elif choice == 3:
        angle_sum = (sides - 2) * 180
        print("Sum of Interior Angles:", angle_sum, "degrees")

    elif choice == 4:
        angle_sum = (sides - 2) * 180
        each_angle = angle_sum / sides

        print("Sum of Interior Angles:", angle_sum, "degrees")
        print("Each Interior Angle:", round(each_angle, 2), "degrees")

    else:
        print("Invalid choice.")

polygonpartitionplanner()