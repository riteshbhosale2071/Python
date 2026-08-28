def polygonsidesearch():
    angle = float(input("Enter each interior angle of the regular polygon: "))

    if angle <= 0 or angle >= 180:
        print("Interior angle must be between 0° and 180°.")
        return

    # For a regular polygon:
    # Exterior angle = 180 - Interior angle
    exterior_angle = 180 - angle

    sides = 360 / exterior_angle

    if sides.is_integer() and sides >= 3:
        print("Number of Sides:", int(sides))
    else:
        print("No regular polygon has this exact interior angle.")

polygonsidesearch()