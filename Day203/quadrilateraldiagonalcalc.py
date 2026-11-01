import math

def quadrilateraldiagonalcalc():
    print("Quadrilateral Diagonal Calculator")
    print("1. Rectangle")
    print("2. Square")
    print("3. Parallelogram")
    print("4. Rhombus")

    choice = input("Select quadrilateral type (1-4): ")

    if choice == "1":
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        if length <= 0 or width <= 0:
            print("Invalid dimensions. Values must be positive.")
            return

        diagonal = math.sqrt(length**2 + width**2)
        print(f"Diagonal length: {diagonal:.2f}")

    elif choice == "2":
        side = float(input("Enter square side length: "))

        if side <= 0:
            print("Invalid side length. It must be positive.")
            return

        diagonal = side * math.sqrt(2)
        print(f"Diagonal length: {diagonal:.2f}")

    elif choice == "3":
        side_a = float(input("Enter first side length: "))
        side_b = float(input("Enter adjacent side length: "))
        angle = float(input("Enter included angle in degrees: "))

        if side_a <= 0 or side_b <= 0 or angle <= 0 or angle >= 180:
            print("Invalid measurements.")
            return

        angle_radians = math.radians(angle)
        diagonal_1 = math.sqrt(
            side_a**2 + side_b**2
            + 2 * side_a * side_b * math.cos(angle_radians)
        )
        diagonal_2 = math.sqrt(
            side_a**2 + side_b**2
            - 2 * side_a * side_b * math.cos(angle_radians)
        )

        print(f"First diagonal: {diagonal_1:.2f}")
        print(f"Second diagonal: {diagonal_2:.2f}")

    elif choice == "4":
        side = float(input("Enter rhombus side length: "))
        angle = float(input("Enter one interior angle in degrees: "))

        if side <= 0 or angle <= 0 or angle >= 180:
            print("Invalid measurements.")
            return

        angle_radians = math.radians(angle)
        diagonal_1 = side * math.sqrt(2 + 2 * math.cos(angle_radians))
        diagonal_2 = side * math.sqrt(2 - 2 * math.cos(angle_radians))

        print(f"First diagonal: {diagonal_1:.2f}")
        print(f"Second diagonal: {diagonal_2:.2f}")

    else:
        print("Invalid selection. Choose a number from 1 to 4.")

quadrilateraldiagonalcalc()