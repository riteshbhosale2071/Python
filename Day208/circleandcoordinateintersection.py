import math

def circleandcoordinateintersection():
    print("Circle and Coordinate Intersection Tester")
    print("1. Check whether a point lies inside, outside, or on a circle")
    print("2. Find intersection of a circle with X-axis")
    print("3. Find intersection of a circle with Y-axis")
    print("4. Check whether a line intersects a circle")

    choice = input("Enter your choice (1-4): ")

    try:
        h = float(input("Enter circle center X-coordinate: "))
        k = float(input("Enter circle center Y-coordinate: "))
        radius = float(input("Enter circle radius: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        if choice == "1":
            x = float(input("Enter point X-coordinate: "))
            y = float(input("Enter point Y-coordinate: "))

            distance = math.sqrt((x - h) ** 2 + (y - k) ** 2)

            print("Distance from center:", round(distance, 2))

            if math.isclose(distance, radius, abs_tol=1e-9):
                print("Point lies on the circle.")
            elif distance < radius:
                print("Point lies inside the circle.")
            else:
                print("Point lies outside the circle.")

        elif choice == "2":
            if abs(k) > radius:
                print("Circle does not intersect the X-axis.")
                return

            offset = math.sqrt(max(0, radius ** 2 - k ** 2))
            x1 = h - offset
            x2 = h + offset

            print("X-axis intersection points:")
            print(f"({round(x1, 2)}, 0)")
            if not math.isclose(x1, x2, abs_tol=1e-9):
                print(f"({round(x2, 2)}, 0)")

        elif choice == "3":
            if abs(h) > radius:
                print("Circle does not intersect the Y-axis.")
                return

            offset = math.sqrt(max(0, radius ** 2 - h ** 2))
            y1 = k - offset
            y2 = k + offset

            print("Y-axis intersection points:")
            print(f"(0, {round(y1, 2)})")
            if not math.isclose(y1, y2, abs_tol=1e-9):
                print(f"(0, {round(y2, 2)})")

        elif choice == "4":
            print("Enter line equation in the form y = mx + c")
            m = float(input("Enter slope (m): "))
            c = float(input("Enter intercept (c): "))

            a = 1 + m ** 2
            b = 2 * (m * (c - k) - h)
            d = h ** 2 + (c - k) ** 2 - radius ** 2

            discriminant = b ** 2 - 4 * a * d

            if discriminant < -1e-9:
                print("Line does not intersect the circle.")
            elif math.isclose(discriminant, 0, abs_tol=1e-9):
                x = -b / (2 * a)
                y = m * x + c
                print("Line touches the circle at one point.")
                print("Intersection:", (round(x, 2), round(y, 2)))
            else:
                root = math.sqrt(discriminant)
                x1 = (-b + root) / (2 * a)
                x2 = (-b - root) / (2 * a)

                y1 = m * x1 + c
                y2 = m * x2 + c

                print("Line intersects the circle at two points.")
                print("First intersection:", (round(x1, 2), round(y1, 2)))
                print("Second intersection:", (round(x2, 2), round(y2, 2)))

        else:
            print("Invalid choice. Please select from 1 to 4.")

    except ValueError:
        print("Please enter valid numeric values.")

circleandcoordinateintersection()