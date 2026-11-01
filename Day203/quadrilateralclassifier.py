def quadrilateralclassifier():
    print("Quadrilateral Classifier")
    print("Enter the four interior angles of the quadrilateral.")

    angles = []

    for i in range(1, 5):
        angle = float(input(f"Enter angle {i}: "))

        if angle <= 0 or angle >= 180:
            print("Invalid angle. Each interior angle must be between 0 and 180 degrees.")
            return

        angles.append(angle)

    if abs(sum(angles) - 360) > 1e-6:
        print("Invalid quadrilateral. Interior angles must sum to 360 degrees.")
        return

    if all(abs(angle - 90) < 1e-6 for angle in angles):
        print("Classification: Rectangle or Square")
        print("All angles are right angles. Side lengths are needed to distinguish them.")
    elif angles[0] == angles[2] and angles[1] == angles[3]:
        print("Classification: Possible parallelogram")
        print("Opposite angles are equal.")
    else:
        print("Classification: General quadrilateral")

quadrilateralclassifier()