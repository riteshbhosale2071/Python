def parallelogrampropertyvalidator():
    print("Parallelogram Property Validator")
    print("Enter the four side lengths and four interior angles.")

    sides = []
    angles = []

    for i in range(1, 5):
        side = float(input(f"Enter side {i} length: "))
        if side <= 0:
            print("Invalid side length. Lengths must be positive.")
            return
        sides.append(side)

    for i in range(1, 5):
        angle = float(input(f"Enter interior angle {i} in degrees: "))
        if angle <= 0 or angle >= 180:
            print("Invalid angle. Each angle must be between 0 and 180 degrees.")
            return
        angles.append(angle)

    opposite_sides_equal = (
        abs(sides[0] - sides[2]) < 1e-6
        and abs(sides[1] - sides[3]) < 1e-6
    )

    opposite_angles_equal = (
        abs(angles[0] - angles[2]) < 1e-6
        and abs(angles[1] - angles[3]) < 1e-6
    )

    adjacent_angles_supplementary = all(
        abs(angles[i] + angles[(i + 1) % 4] - 180) < 1e-6
        for i in range(4)
    )

    angle_sum_valid = abs(sum(angles) - 360) < 1e-6

    print("\nValidation Report")
    print("Opposite sides equal:", opposite_sides_equal)
    print("Opposite angles equal:", opposite_angles_equal)
    print("Adjacent angles supplementary:", adjacent_angles_supplementary)
    print("Interior angle sum is 360 degrees:", angle_sum_valid)

    if (
        opposite_sides_equal
        and opposite_angles_equal
        and adjacent_angles_supplementary
        and angle_sum_valid
    ):
        print("The given measurements satisfy parallelogram properties.")
    else:
        print("The given measurements do not satisfy all parallelogram properties.")

parallelogrampropertyvalidator()