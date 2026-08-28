def polygonexteriorangle():
    sides = int(input("Enter the number of sides of the polygon: "))

    if sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    # Sum of exterior angles of any polygon is 360°
    exterior_angle_sum = 360
    each_exterior_angle = exterior_angle_sum / sides

    print("Sum of Exterior Angles:", exterior_angle_sum, "°")
    print("Each Exterior Angle of a Regular Polygon:",
          each_exterior_angle, "°")

polygonexteriorangle()