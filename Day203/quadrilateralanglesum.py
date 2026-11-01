def quadrilateralanglesum():
    angles = []

    for i in range(1, 5):
        angle = float(input(f"Enter interior angle {i} in degrees: "))

        if angle <= 0 or angle >= 360:
            print("Invalid angle. Each interior angle must be between 0 and 360 degrees.")
            return

        angles.append(angle)

    total = sum(angles)
    expected_sum = 360

    print(f"\nSum of given angles: {total:.2f} degrees")

    if abs(total - expected_sum) < 1e-6:
        print("Valid quadrilateral angle sum.")
    else:
        print(f"Invalid angle sum. A quadrilateral's interior angles must total {expected_sum} degrees.")
        print(f"Difference: {abs(expected_sum - total):.2f} degrees")

quadrilateralanglesum()