import math

def trigonometricratiorelationship():
    print("Trigonometric Ratio Relationship Checker")
    print("1. Check tan(x) = sin(x) / cos(x)")
    print("2. Check cot(x) = cos(x) / sin(x)")
    print("3. Check sin(x) × cosec(x) = 1")
    print("4. Check cos(x) × sec(x) = 1")
    print("5. Check tan(x) × cot(x) = 1")

    choice = input("Enter your choice (1-5): ")

    try:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        sin_x = math.sin(radians)
        cos_x = math.cos(radians)

        if choice == "1":
            if math.isclose(cos_x, 0, abs_tol=1e-10):
                print("Relationship is undefined for this angle.")
                return

            left_side = math.tan(radians)
            right_side = sin_x / cos_x

        elif choice == "2":
            if math.isclose(sin_x, 0, abs_tol=1e-10):
                print("Relationship is undefined for this angle.")
                return

            left_side = 1 / math.tan(radians)
            right_side = cos_x / sin_x

        elif choice == "3":
            if math.isclose(sin_x, 0, abs_tol=1e-10):
                print("Relationship is undefined for this angle.")
                return

            left_side = sin_x * (1 / sin_x)
            right_side = 1

        elif choice == "4":
            if math.isclose(cos_x, 0, abs_tol=1e-10):
                print("Relationship is undefined for this angle.")
                return

            left_side = cos_x * (1 / cos_x)
            right_side = 1

        elif choice == "5":
            if math.isclose(sin_x, 0, abs_tol=1e-10) or math.isclose(cos_x, 0, abs_tol=1e-10):
                print("Relationship is undefined for this angle.")
                return

            left_side = math.tan(radians) * (1 / math.tan(radians))
            right_side = 1

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
            return

        print("Left side:", round(left_side, 6))
        print("Right side:", round(right_side, 6))

        if math.isclose(left_side, right_side, rel_tol=1e-9, abs_tol=1e-9):
            print("Relationship verified.")
        else:
            print("Relationship not verified.")

    except ValueError:
        print("Please enter a valid numeric angle.")

trigonometricratiorelationship()