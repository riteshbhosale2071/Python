def polygoninteriorangle():
    sides = int(input("Enter the number of sides of the polygon: "))

    if sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    # Sum of interior angles
    angle_sum = (sides - 2) * 180

    # For a regular polygon, each interior angle
    interior_angle = angle_sum / sides

    print("Sum of Interior Angles:", angle_sum, "°")
    print("Each Interior Angle of a Regular Polygon:", interior_angle, "°")

polygoninteriorangle()