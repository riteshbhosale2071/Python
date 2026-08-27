def exterioranglevalidator():
    interior_angle = float(input("Enter the interior angle: "))
    exterior_angle = float(input("Enter the exterior angle: "))

    if interior_angle <= 0 or interior_angle >= 180:
        print("Interior angle must be between 0° and 180°.")
        return

    if exterior_angle <= 0 or exterior_angle >= 180:
        print("Exterior angle must be between 0° and 180°.")
        return

    if abs(interior_angle + exterior_angle - 180) < 1e-9:
        print("Valid Exterior Angle.")
        print("Interior + Exterior Angle = 180°")
    else:
        print("Invalid Exterior Angle.")

exterioranglevalidator()