def medianintersectionchecker():
    print("Median Intersection Checker :")

    print("\nEnter coordinates of Triangle Vertex A:")
    ax = float(input("Ax: "))
    ay = float(input("Ay: "))

    print("\nEnter coordinates of Triangle Vertex B:")
    bx = float(input("Bx: "))
    by = float(input("By: "))

    print("\nEnter coordinates of Triangle Vertex C:")
    cx = float(input("Cx: "))
    cy = float(input("Cy: "))

    midpoint_bc_x = (bx + cx) / 2
    midpoint_bc_y = (by + cy) / 2

    midpoint_ac_x = (ax + cx) / 2
    midpoint_ac_y = (ay + cy) / 2

    midpoint_ab_x = (ax + bx) / 2
    midpoint_ab_y = (ay + by) / 2

    centroid_x = (ax + bx + cx) / 3
    centroid_y = (ay + by + cy) / 3

    print("\nMedian Information :")

    print(
        f"Median from A → BC midpoint: "
        f"({midpoint_bc_x:.2f}, {midpoint_bc_y:.2f})"
    )

    print(
        f"Median from B → AC midpoint: "
        f"({midpoint_ac_x:.2f}, {midpoint_ac_y:.2f})"
    )

    print(
        f"Median from C → AB midpoint: "
        f"({midpoint_ab_x:.2f}, {midpoint_ab_y:.2f})"
    )

    print("\nMedian Intersection :")
    print(f"Common Intersection Point: ({centroid_x:.2f}, {centroid_y:.2f})")

    print("\nResult:")
    print("All three medians intersect at the centroid.")
    print("The centroid divides every median in a 2:1 ratio.")

medianintersectionchecker()