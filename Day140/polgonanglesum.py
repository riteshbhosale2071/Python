def polygonanglesum():
    sides = int(input("Enter the number of sides of the polygon: "))
    angle_sum = float(input("Enter the given sum of interior angles: "))

    if sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    expected_sum = (sides - 2) * 180

    print("Expected Interior Angle Sum:", expected_sum, "°")

    if angle_sum == expected_sum:
        print("Valid Angle Sum.")
    else:
        print("Invalid Angle Sum.")

polygonanglesum()