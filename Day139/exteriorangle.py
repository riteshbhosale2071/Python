def exteriorangle():
    interior_angle = float(input("Enter the interior angle: "))

    if interior_angle <= 0 or interior_angle >= 180:
        print("Interior angle must be between 0° and 180°.")
        return

    exterior_angle = 180 - interior_angle

    print("Exterior Angle:", exterior_angle, "°")

exteriorangle()