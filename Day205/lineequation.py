def lineequation():
    x1 = float(input("Enter the X-coordinate of the first point: "))
    y1 = float(input("Enter the Y-coordinate of the first point: "))

    x2 = float(input("Enter the X-coordinate of the second point: "))
    y2 = float(input("Enter the Y-coordinate of the second point: "))

    if x1 == x2 and y1 == y2:
        print("Invalid input. Two distinct points are required.")
        return

    if x1 == x2:
        print(f"Vertical Line Equation: x = {x1:g}")
        return

    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1

    if slope == 0:
        equation = f"y = {intercept:g}"
    elif intercept == 0:
        equation = f"y = {slope:g}x"
    elif intercept < 0:
        equation = f"y = {slope:g}x - {abs(intercept):g}"
    else:
        equation = f"y = {slope:g}x + {intercept:g}"

    print(f"First Point: ({x1:g}, {y1:g})")
    print(f"Second Point: ({x2:g}, {y2:g})")
    print(f"Slope: {slope:g}")
    print(f"Line Equation: {equation}")

lineequation()