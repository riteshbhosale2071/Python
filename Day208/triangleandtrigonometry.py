import math

def triangleandtrigonometry():
    print("Triangle and Trigonometry Solver")
    print("1. Calculate Third Angle of Triangle")
    print("2. Calculate Triangle Area")
    print("3. Calculate Hypotenuse")
    print("4. Calculate Missing Side")
    print("5. Calculate Trigonometric Ratios")
    print("6. Calculate Missing Angle")
    print("7. Calculate All Triangle Measurements")

    choice = input("Enter your choice (1-7): ")

    try:
        if choice == "1":
            angle1 = float(input("Enter first angle: "))
            angle2 = float(input("Enter second angle: "))

            if angle1 <= 0 or angle2 <= 0 or angle1 + angle2 >= 180:
                print("Invalid triangle angles.")
                return

            angle3 = 180 - angle1 - angle2
            print("Third Angle:", round(angle3, 2), "degrees")

        elif choice == "2":
            base = float(input("Enter triangle base: "))
            height = float(input("Enter triangle height: "))

            if base <= 0 or height <= 0:
                print("Measurements must be positive.")
                return

            area = 0.5 * base * height
            print("Triangle Area:", round(area, 2), "square units")

        elif choice == "3":
            side1 = float(input("Enter first perpendicular side: "))
            side2 = float(input("Enter second perpendicular side: "))

            if side1 <= 0 or side2 <= 0:
                print("Side lengths must be positive.")
                return

            hypotenuse = math.sqrt(side1 ** 2 + side2 ** 2)
            print("Hypotenuse:", round(hypotenuse, 2), "units")

        elif choice == "4":
            hypotenuse = float(input("Enter hypotenuse: "))
            known_side = float(input("Enter known side: "))

            if hypotenuse <= 0 or known_side <= 0 or known_side >= hypotenuse:
                print("Invalid side measurements.")
                return

            missing_side = math.sqrt(hypotenuse ** 2 - known_side ** 2)
            print("Missing Side:", round(missing_side, 2), "units")

        elif choice == "5":
            angle = float(input("Enter angle in degrees: "))

            if angle <= 0 or angle >= 90:
                print("Enter an angle between 0 and 90 degrees.")
                return

            radians = math.radians(angle)

            sin_value = math.sin(radians)
            cos_value = math.cos(radians)
            tan_value = math.tan(radians)

            print("Sine:", round(sin_value, 4))
            print("Cosine:", round(cos_value, 4))
            print("Tangent:", round(tan_value, 4))
            print("Cosecant:", round(1 / sin_value, 4))
            print("Secant:", round(1 / cos_value, 4))
            print("Cotangent:", round(1 / tan_value, 4))

        elif choice == "6":
            opposite = float(input("Enter opposite side: "))
            adjacent = float(input("Enter adjacent side: "))

            if opposite <= 0 or adjacent <= 0:
                print("Side lengths must be positive.")
                return

            angle = math.degrees(math.atan(opposite / adjacent))
            print("Missing Angle:", round(angle, 2), "degrees")

        elif choice == "7":
            side1 = float(input("Enter first side: "))
            side2 = float(input("Enter second side: "))
            side3 = float(input("Enter third side: "))

            if side1 <= 0 or side2 <= 0 or side3 <= 0:
                print("Side lengths must be positive.")
                return

            if (side1 + side2 <= side3 or
                side1 + side3 <= side2 or
                side2 + side3 <= side1):
                print("These sides cannot form a triangle.")
                return

            perimeter = side1 + side2 + side3
            semi_perimeter = perimeter / 2

            area = math.sqrt(
                semi_perimeter *
                (semi_perimeter - side1) *
                (semi_perimeter - side2) *
                (semi_perimeter - side3)
            )

            angle1 = math.degrees(math.acos(
                (side2 ** 2 + side3 ** 2 - side1 ** 2) /
                (2 * side2 * side3)
            ))

            angle2 = math.degrees(math.acos(
                (side1 ** 2 + side3 ** 2 - side2 ** 2) /
                (2 * side1 * side3)
            ))

            angle3 = 180 - angle1 - angle2

            print("\nTriangle Measurements")
            print("Perimeter:", round(perimeter, 2), "units")
            print("Area:", round(area, 2), "square units")
            print("First Angle:", round(angle1, 2), "degrees")
            print("Second Angle:", round(angle2, 2), "degrees")
            print("Third Angle:", round(angle3, 2), "degrees")

        else:
            print("Invalid choice. Please select from 1 to 7.")

    except ValueError:
        print("Please enter valid numeric values.")

triangleandtrigonometry()