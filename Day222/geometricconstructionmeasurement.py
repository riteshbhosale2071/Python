import math

def geometricconstructionmeasurement():
    print("Geometric Construction Measurement Analyzer")
    print("1. Analyze Triangle Measurements")
    print("2. Analyze Circle Measurements")
    print("3. Analyze Line Segment Measurements")
    print("4. Analyze Angle Measurements")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        a = float(input("Enter side A: "))
        b = float(input("Enter side B: "))
        c = float(input("Enter side C: "))

        if min(a, b, c) <= 0:
            print("Side lengths must be positive.")
            return

        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print("Valid Triangle")
            print("Perimeter =", round(a + b + c, 2))
            print("Area =", round(area, 2))
        else:
            print("Invalid Triangle Measurements")

    elif choice == "2":
        radius = float(input("Enter circle radius: "))

        if radius <= 0:
            print("Radius must be positive.")
            return

        print("Diameter =", round(2 * radius, 2))
        print("Circumference =", round(2 * math.pi * radius, 2))
        print("Area =", round(math.pi * radius ** 2, 2))

    elif choice == "3":
        x1 = float(input("Enter first point x-coordinate: "))
        y1 = float(input("Enter first point y-coordinate: "))
        x2 = float(input("Enter second point x-coordinate: "))
        y2 = float(input("Enter second point y-coordinate: "))

        length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        midpoint_x = (x1 + x2) / 2
        midpoint_y = (y1 + y2) / 2

        print("Line Segment Length =", round(length, 2))
        print("Midpoint =", (round(midpoint_x, 2), round(midpoint_y, 2)))

    elif choice == "4":
        angle = float(input("Enter angle measurement in degrees: "))

        if not 0 < angle < 360:
            print("Enter an angle greater than 0 and less than 360 degrees.")
            return

        print("Angle =", angle, "degrees")

        if angle < 90:
            print("Type: Acute Angle")
        elif angle == 90:
            print("Type: Right Angle")
        elif angle < 180:
            print("Type: Obtuse Angle")
        elif angle == 180:
            print("Type: Straight Angle")
        else:
            print("Type: Reflex Angle")

    else:
        print("Invalid choice.")

geometricconstructionmeasurement()