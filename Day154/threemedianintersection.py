def threemedianintersection():
    print("Three Median Intersection Simulator :")

    x1 = float(input("Enter x-coordinate of A: "))
    y1 = float(input("Enter y-coordinate of A: "))

    x2 = float(input("Enter x-coordinate of B: "))
    y2 = float(input("Enter y-coordinate of B: "))

    x3 = float(input("Enter x-coordinate of C: "))
    y3 = float(input("Enter y-coordinate of C: "))

    if (x1 == x2 and y1 == y2) or (x2 == x3 and y2 == y3) or (x1 == x3 and y1 == y3):
        print("Invalid triangle.")
        return

    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)

    if area == 0:
        print("Invalid triangle. Points are collinear.")
        return

    midpoint_bc_x = (x2 + x3) / 2
    midpoint_bc_y = (y2 + y3) / 2

    midpoint_ac_x = (x1 + x3) / 2
    midpoint_ac_y = (y1 + y3) / 2

    midpoint_ab_x = (x1 + x2) / 2
    midpoint_ab_y = (y1 + y2) / 2

    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3

    print("\nMedian Information :")
    print("Median from A meets BC at: ({:.2f}, {:.2f})".format(
        midpoint_bc_x, midpoint_bc_y
    ))

    print("Median from B meets AC at: ({:.2f}, {:.2f})".format(
        midpoint_ac_x, midpoint_ac_y
    ))

    print("Median from C meets AB at: ({:.2f}, {:.2f})".format(
        midpoint_ab_x, midpoint_ab_y
    ))

    print("\nIntersection of Three Medians :")
    print("Centroid: ({:.2f}, {:.2f})".format(centroid_x, centroid_y))

    print("\nAll three medians intersect at the centroid.")
    print("Each median is divided in the ratio 2:1.")

threemedianintersection()