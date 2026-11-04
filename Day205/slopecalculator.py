def slopecalculator():
    x1 = float(input("Enter the X-coordinate of the first point: "))
    y1 = float(input("Enter the Y-coordinate of the first point: "))

    x2 = float(input("Enter the X-coordinate of the second point: "))
    y2 = float(input("Enter the Y-coordinate of the second point: "))

    if x2 == x1:
        print("The slope is undefined. The line is vertical.")
        return

    slope = (y2 - y1) / (x2 - x1)

    print(f"First Point: ({x1:.2f}, {y1:.2f})")
    print(f"Second Point: ({x2:.2f}, {y2:.2f})")
    print(f"Slope: {slope:.2f}")

slopecalculator()