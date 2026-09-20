def diagonalintersectionanalyzer():
    print("Diagonal Intersection Analyzer :")

    x1 = float(input("Enter x-coordinate of point 1: "))
    y1 = float(input("Enter y-coordinate of point 1: "))

    x2 = float(input("Enter x-coordinate of point 2: "))
    y2 = float(input("Enter y-coordinate of point 2: "))

    x3 = float(input("Enter x-coordinate of point 3: "))
    y3 = float(input("Enter y-coordinate of point 3: "))

    x4 = float(input("Enter x-coordinate of point 4: "))
    y4 = float(input("Enter y-coordinate of point 4: "))

    denominator = (x1 - x3) * (y2 - y4) - (y1 - y3) * (x2 - x4)

    if denominator == 0:
        print("The diagonals are parallel or overlapping.")
        print("A unique intersection point cannot be determined.")
    else:
        numerator_x = ((x1 * y3 - y1 * x3) * (x2 - x4)) - ((x1 - x3) * (x2 * y4 - y2 * x4))
        numerator_y = ((x1 * y3 - y1 * x3) * (y2 - y4)) - ((y1 - y3) * (x2 * y4 - y2 * x4))

        intersection_x = numerator_x / denominator
        intersection_y = numerator_y / denominator

        print("The diagonals intersect at:")
        print("X-coordinate:", intersection_x)
        print("Y-coordinate:", intersection_y)

        midpoint_x = (x1 + x3) / 2
        midpoint_y = (y1 + y3) / 2

        second_midpoint_x = (x2 + x4) / 2
        second_midpoint_y = (y2 + y4) / 2

        if midpoint_x == second_midpoint_x and midpoint_y == second_midpoint_y:
            print("The diagonals bisect each other.")
        else:
            print("The diagonals do not bisect each other.")

diagonalintersectionanalyzer()