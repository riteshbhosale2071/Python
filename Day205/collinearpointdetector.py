def collinearpointdetector():
    x1 = float(input("Enter the X-coordinate of point A: "))
    y1 = float(input("Enter the Y-coordinate of point A: "))

    x2 = float(input("Enter the X-coordinate of point B: "))
    y2 = float(input("Enter the Y-coordinate of point B: "))

    x3 = float(input("Enter the X-coordinate of point C: "))
    y3 = float(input("Enter the Y-coordinate of point C: "))

    area_twice = (
        x1 * (y2 - y3) +
        x2 * (y3 - y1) +
        x3 * (y1 - y2)
    )

    if abs(area_twice) < 1e-9:
        print("The three points are collinear.")
    else:
        print("The three points are not collinear.")

collinearpointdetector()