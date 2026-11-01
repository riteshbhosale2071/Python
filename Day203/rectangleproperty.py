def rectangleproperty():
    print("Rectangle Property Checker")

    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))

    if length <= 0 or width <= 0:
        print("Invalid dimensions. Length and width must be positive.")
        return

    side_a = float(input("Enter first opposite side length: "))
    side_b = float(input("Enter second opposite side length: "))

    angle_a = float(input("Enter first interior angle: "))
    angle_b = float(input("Enter second interior angle: "))
    angle_c = float(input("Enter third interior angle: "))
    angle_d = float(input("Enter fourth interior angle: "))

    opposite_sides_equal = abs(side_a - side_b) < 1e-6
    all_angles_right = all(
        abs(angle - 90) < 1e-6
        for angle in [angle_a, angle_b, angle_c, angle_d]
    )

    print("\nRectangle Property Report")
    print("Length:", length)
    print("Width:", width)
    print("Area:", length * width)
    print("Perimeter:", 2 * (length + width))
    print("Opposite sides equal:", opposite_sides_equal)
    print("All angles are 90 degrees:", all_angles_right)

    if all_angles_right:
        print("The angle property of a rectangle is satisfied.")
    else:
        print("The angle property of a rectangle is not satisfied.")

rectangleproperty()