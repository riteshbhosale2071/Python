def congruencepropertytransfer():
    print("Congruence Property Transfer :")

    print("\nEnter Triangle 1:")
    side1_a = float(input("Enter side AB: "))
    side1_b = float(input("Enter side BC: "))
    side1_c = float(input("Enter side CA: "))

    angle1_a = float(input("Enter angle A: "))
    angle1_b = float(input("Enter angle B: "))
    angle1_c = float(input("Enter angle C: "))

    print("\nEnter Triangle 2:")
    side2_a = float(input("Enter side PQ: "))
    side2_b = float(input("Enter side QR: "))
    side2_c = float(input("Enter side RP: "))

    angle2_a = float(input("Enter angle P: "))
    angle2_b = float(input("Enter angle Q: "))
    angle2_c = float(input("Enter angle R: "))

    if side1_a <= 0 or side1_b <= 0 or side1_c <= 0:
        print("Triangle 1 side lengths must be positive.")
        return

    if side2_a <= 0 or side2_b <= 0 or side2_c <= 0:
        print("Triangle 2 side lengths must be positive.")
        return

    if angle1_a <= 0 or angle1_b <= 0 or angle1_c <= 0:
        print("Triangle 1 angles must be positive.")
        return

    if angle2_a <= 0 or angle2_b <= 0 or angle2_c <= 0:
        print("Triangle 2 angles must be positive.")
        return

    side_match = (
        side1_a == side2_a and
        side1_b == side2_b and
        side1_c == side2_c
    )

    angle_match = (
        angle1_a == angle2_a and
        angle1_b == angle2_b and
        angle1_c == angle2_c
    )

    print("\nProperty Transfer Analysis :")

    if side_match and angle_match:
        print("Triangles are congruent.")
        print("Corresponding sides are equal.")
        print("Corresponding angles are equal.")
        print("\nTransferred Properties:")
        print("AB = PQ")
        print("BC = QR")
        print("CA = RP")
        print("Angle A = Angle P")
        print("Angle B = Angle Q")
        print("Angle C = Angle R")
    else:
        print("Complete congruence cannot be established.")

        if side_match:
            print("Side property transferred: All corresponding sides are equal.")
        else:
            print("Side property not fully transferred.")

        if angle_match:
            print("Angle property transferred: All corresponding angles are equal.")
        else:
            print("Angle property not fully transferred.")

congruencepropertytransfer()