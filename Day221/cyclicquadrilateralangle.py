def cyclicquadrilateralangle():
    print("Cyclic Quadrilateral Angle Calculator")
    print("1. Find Opposite Angle")
    print("2. Find Missing Angle")
    print("3. Verify Cyclic Quadrilateral")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        angle = float(input("Enter one interior angle: "))

        if angle <= 0 or angle >= 180:
            print("Angle must be between 0 and 180 degrees.")
            return

        opposite = 180 - angle
        print("Opposite Angle =", round(opposite, 2), "degrees")

    elif choice == "2":
        angle_a = float(input("Enter angle A: "))
        angle_b = float(input("Enter angle B: "))
        angle_c = float(input("Enter angle C: "))

        if any(angle <= 0 or angle >= 180 for angle in [angle_a, angle_b, angle_c]):
            print("All angles must be between 0 and 180 degrees.")
            return

        angle_d = 360 - (angle_a + angle_b + angle_c)

        if 0 < angle_d < 180:
            print("Missing Angle D =", round(angle_d, 2), "degrees")
        else:
            print("Invalid angles for a cyclic quadrilateral.")

    elif choice == "3":
        angle_a = float(input("Enter angle A: "))
        angle_b = float(input("Enter opposite angle B: "))

        if not (0 < angle_a < 180 and 0 < angle_b < 180):
            print("Angles must be between 0 and 180 degrees.")
            return

        print("\nSum of Opposite Angles =", angle_a + angle_b)

        if abs(angle_a + angle_b - 180) < 1e-9:
            print("The quadrilateral satisfies the cyclic quadrilateral property.")
        else:
            print("The quadrilateral does not satisfy the cyclic quadrilateral property.")

    else:
        print("Invalid choice.")

cyclicquadrilateralangle()