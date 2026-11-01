def rhombuspropertychecker():
    print("Rhombus Property Checker")

    sides = []
    for i in range(1, 5):
        side = float(input(f"Enter side {i} length: "))

        if side <= 0:
            print("Invalid side length. All sides must be positive.")
            return

        sides.append(side)

    angles = []
    for i in range(1, 5):
        angle = float(input(f"Enter interior angle {i} in degrees: "))

        if angle <= 0 or angle >= 180:
            print("Invalid angle. Each angle must be between 0 and 180 degrees.")
            return

        angles.append(angle)

    all_sides_equal = all(
        abs(side - sides[0]) < 1e-6
        for side in sides
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

    print("\nRhombus Property Report")
    print("All four sides equal:", all_sides_equal)
    print("Opposite angles equal:", opposite_angles_equal)
    print("Adjacent angles supplementary:", adjacent_angles_supplementary)
    print("Interior angle sum is 360 degrees:", angle_sum_valid)

    if (
        all_sides_equal
        and opposite_angles_equal
        and adjacent_angles_supplementary
        and angle_sum_valid
    ):
        print("The measurements satisfy the rhombus properties.")
    else:
        print("The measurements do not satisfy all rhombus properties.")

rhombuspropertychecker()