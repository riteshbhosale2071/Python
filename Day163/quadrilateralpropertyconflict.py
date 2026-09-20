def quadrilateralpropertyconflict():
    print("Quadrilateral Property Conflict Detector :")

    side1 = float(input("Enter side 1: "))
    side2 = float(input("Enter side 2: "))
    side3 = float(input("Enter side 3: "))
    side4 = float(input("Enter side 4: "))

    angle1 = float(input("Enter angle 1: "))
    angle2 = float(input("Enter angle 2: "))
    angle3 = float(input("Enter angle 3: "))
    angle4 = float(input("Enter angle 4: "))

    diagonal1 = float(input("Enter diagonal 1: "))
    diagonal2 = float(input("Enter diagonal 2: "))

    conflict = False

    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side4 <= 0:
        print("Conflict: Side lengths must be greater than zero.")
        conflict = True

    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0 or angle4 <= 0:
        print("Conflict: Angles must be greater than zero.")
        conflict = True

    angle_sum = angle1 + angle2 + angle3 + angle4

    if angle_sum != 360:
        print("Conflict: The sum of angles is not 360 degrees.")
        conflict = True

    if diagonal1 <= 0 or diagonal2 <= 0:
        print("Conflict: Diagonal lengths must be greater than zero.")
        conflict = True

    if side1 == side2 == side3 == side4:
        if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
            if diagonal1 != diagonal2:
                print("Conflict: A square should have equal diagonals.")
                conflict = True

    if side1 == side3 and side2 == side4:
        if angle1 != angle3 or angle2 != angle4:
            print("Conflict: Opposite angles should be equal in a parallelogram.")
            conflict = True

    if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
        if side1 != side3 or side2 != side4:
            print("Conflict: Opposite sides should be equal in a rectangle.")
            conflict = True

    if diagonal1 == diagonal2:
        if side1 == side2 == side3 == side4:
            print("Equal diagonals and equal sides are consistent with a square.")
        elif angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
            print("Equal diagonals and right angles are consistent with a rectangle.")

    if conflict:
        print("Property conflicts were detected.")
    else:
        print("No major property conflicts were detected.")

quadrilateralpropertyconflict()