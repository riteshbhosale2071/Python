def parallellinesandtransversals():
    print("Parallel Lines and Transversals Calculator")

    angle = float(input("Enter any one angle (in degrees): "))

    if angle <= 0 or angle >= 180:
        print("Angle must be greater than 0 and less than 180.")
        return

    corresponding = angle
    alternate_interior = angle
    alternate_exterior = angle
    vertically_opposite = angle
    co_interior = 180 - angle
    adjacent = 180 - angle

    print("\nCalculated Angles:")
    print("Corresponding Angle =", round(corresponding, 2), "degrees")
    print("Alternate Interior Angle =", round(alternate_interior, 2), "degrees")
    print("Alternate Exterior Angle =", round(alternate_exterior, 2), "degrees")
    print("Vertically Opposite Angle =", round(vertically_opposite, 2), "degrees")
    print("Co-interior Angle =", round(co_interior, 2), "degrees")
    print("Adjacent Angle =", round(adjacent, 2), "degrees")

    print("\nProperties:")
    print("Corresponding angles are equal.")
    print("Alternate interior angles are equal.")
    print("Alternate exterior angles are equal.")
    print("Co-interior angles add up to 180 degrees.")

parallellinesandtransversals()