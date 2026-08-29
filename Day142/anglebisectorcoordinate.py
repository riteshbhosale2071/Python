import math

def anglebisectorcoordinate():
    print("Enter the coordinates of the vertex and two points on the arms.")

    vx = float(input("Enter x-coordinate of vertex: "))
    vy = float(input("Enter y-coordinate of vertex: "))

    x1 = float(input("Enter x-coordinate of first point: "))
    y1 = float(input("Enter y-coordinate of first point: "))

    x2 = float(input("Enter x-coordinate of second point: "))
    y2 = float(input("Enter y-coordinate of second point: "))

    dx1 = x1 - vx
    dy1 = y1 - vy

    dx2 = x2 - vx
    dy2 = y2 - vy

    length1 = math.hypot(dx1, dy1)
    length2 = math.hypot(dx2, dy2)

    if length1 == 0 or length2 == 0:
        print("Points defining the angle cannot be the vertex.")
        return

    ux1 = dx1 / length1
    uy1 = dy1 / length1

    ux2 = dx2 / length2
    uy2 = dy2 / length2

    bx = ux1 + ux2
    by = uy1 + uy2

    bisector_length = math.hypot(bx, by)

    if math.isclose(bisector_length, 0):
        print("The points form a straight angle.")
        return

    bx /= bisector_length
    by /= bisector_length

    print("\nAngle Bisector Direction Vector:", (bx, by))
    print("The angle bisector starts from the vertex",
          f"({vx}, {vy})",
          "in the direction shown above.")

anglebisectorcoordinate()