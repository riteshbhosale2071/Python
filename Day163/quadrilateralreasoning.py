def quadrilateralreasoning():
    print("Quadrilateral Reasoning Engine :")

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

    print("\nReasoning Results :")

    if side1 <= 0 or side2 <= 0 or side3 <= 0 or side4 <= 0:
        print("Invalid side lengths.")
        return

    if angle1 <= 0 or angle2 <= 0 or angle3 <= 0 or angle4 <= 0:
        print("Invalid angle values.")
        return

    angle_sum = angle1 + angle2 + angle3 + angle4

    if angle_sum != 360:
        print("The angle sum is invalid.")
        return

    if side1 == side2 == side3 == side4:
        if angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
            print("Reasoning: All sides are equal and all angles are right angles.")
            print("Classification: Square")
        else:
            print("Reasoning: All four sides are equal.")
            print("Classification: Rhombus")

    elif angle1 == 90 and angle2 == 90 and angle3 == 90 and angle4 == 90:
        if side1 == side3 and side2 == side4:
            print("Reasoning: All angles are right angles and opposite sides are equal.")
            print("Classification: Rectangle")
        else:
            print("Reasoning: All angles are right angles.")
            print("Classification: Quadrilateral with right angles")

    elif side1 == side3 and side2 == side4:
        if angle1 == angle3 and angle2 == angle4:
            print("Reasoning: Both pairs of opposite sides and angles are equal.")
            print("Classification: Parallelogram")
        else:
            print("Reasoning: Opposite sides are equal.")
            print("Classification: Possible parallelogram")

    elif side1 == side2 and side3 == side4:
        print("Reasoning: Two pairs of adjacent sides are equal.")
        print("Classification: Kite")

    elif side1 == side3 or side2 == side4:
        print("Reasoning: A pair of opposite sides may be equal.")
        print("Classification: Possible trapezium or irregular quadrilateral")

    else:
        print("Reasoning: The given properties do not match a special quadrilateral.")
        print("Classification: Irregular quadrilateral")

    if diagonal1 > 0 and diagonal2 > 0:
        if diagonal1 == diagonal2:
            print("Diagonal analysis: The diagonals are equal.")
        else:
            print("Diagonal analysis: The diagonals have different lengths.")
    else:
        print("Invalid diagonal lengths.")

quadrilateralreasoning()