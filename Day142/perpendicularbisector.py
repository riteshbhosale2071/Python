import math

def perpendicularbisector():
    x1 = float(input("Enter x-coordinate of first endpoint: "))
    y1 = float(input("Enter y-coordinate of first endpoint: "))

    x2 = float(input("Enter x-coordinate of second endpoint: "))
    y2 = float(input("Enter y-coordinate of second endpoint: "))

    if x1 == x2 and y1 == y2:
        print("Invalid line segment. Endpoints must be different.")
        return

    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2

    dx = x2 - x1
    dy = y2 - y1

    print("\nMidpoint:", (mid_x, mid_y))

    if dy == 0:
        print("Perpendicular Bisector: Vertical line")
        print(f"x = {mid_x}")
    elif dx == 0:
        print("Perpendicular Bisector: Horizontal line")
        print(f"y = {mid_y}")
    else:
        original_slope = dy / dx
        perpendicular_slope = -1 / original_slope

        print("Original Line Slope:", original_slope)
        print("Perpendicular Bisector Slope:", perpendicular_slope)
        print(
            f"Equation: y - {mid_y} = "
            f"{perpendicular_slope}(x - {mid_x})"
        )

perpendicularbisector()