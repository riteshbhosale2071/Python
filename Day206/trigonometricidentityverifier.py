import math

def trigonometricidentityverifier():
    print("Trigonometric Identity Verifier")
    print("1. sin²(x) + cos²(x) = 1")
    print("2. 1 + tan²(x) = sec²(x)")
    print("3. 1 + cot²(x) = cosec²(x)")

    choice = input("Enter your choice (1, 2, or 3): ")

    try:
        angle = float(input("Enter angle in degrees: "))
        radians = math.radians(angle)

        if choice == "1":
            left_side = math.sin(radians) ** 2 + math.cos(radians) ** 2
            right_side = 1

        elif choice == "2":
            if math.isclose(math.cos(radians), 0, abs_tol=1e-10):
                print("Identity is undefined for this angle.")
                return

            tan_value = math.tan(radians)
            sec_value = 1 / math.cos(radians)

            left_side = 1 + tan_value ** 2
            right_side = sec_value ** 2

        elif choice == "3":
            if math.isclose(math.sin(radians), 0, abs_tol=1e-10):
                print("Identity is undefined for this angle.")
                return

            cot_value = 1 / math.tan(radians)
            cosec_value = 1 / math.sin(radians)

            left_side = 1 + cot_value ** 2
            right_side = cosec_value ** 2

        else:
            print("Invalid choice.")
            return

        print("Left side:", round(left_side, 6))
        print("Right side:", round(right_side, 6))

        if math.isclose(left_side, right_side, rel_tol=1e-9, abs_tol=1e-9):
            print("Identity verified.")
        else:
            print("Identity not verified.")

    except ValueError:
        print("Please enter a valid number.")

trigonometricidentityverifier()