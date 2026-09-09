def mediandivisionvalidator():
    print("Median Division Validator :")

    median = float(input("Enter total median length: "))
    vertex_part = float(input("Enter vertex-to-centroid length: "))
    centroid_part = float(input("Enter centroid-to-midpoint length: "))

    if median <= 0 or vertex_part <= 0 or centroid_part <= 0:
        print("All lengths must be positive.")
        return

    tolerance = 1e-9

    print("\nMedian Division Analysis :")
    print("Total Median:", median)
    print("Vertex to Centroid:", vertex_part)
    print("Centroid to Midpoint:", centroid_part)

    total_check = vertex_part + centroid_part

    ratio_check = vertex_part / centroid_part

    if abs(total_check - median) < tolerance and abs(ratio_check - 2) < tolerance:
        print("\nResult: VALID")
        print("The median is correctly divided by the centroid in a 2:1 ratio.")
    else:
        print("\nResult: INVALID")
        print("The median does not satisfy the centroid division rule.")

        print("\nExpected Division:")
        print("Vertex to Centroid = 2/3 of median")
        print("Centroid to Midpoint = 1/3 of median")

mediandivisionvalidator()