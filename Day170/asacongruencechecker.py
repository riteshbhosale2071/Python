def asacongruencechecker():
    print("ASA Congruence Checker :")

    print("\nEnter Triangle 1:")
    angle1_a = float(input("Enter first angle: "))
    side1 = float(input("Enter included side: "))
    angle1_b = float(input("Enter second angle: "))

    print("\nEnter Triangle 2:")
    angle2_a = float(input("Enter first angle: "))
    side2 = float(input("Enter included side: "))
    angle2_b = float(input("Enter second angle: "))

    if side1 <= 0 or side2 <= 0:
        print("Side lengths must be positive.")
        return

    if angle1_a <= 0 or angle1_a >= 180 or angle1_b <= 0 or angle1_b >= 180:
        print("Triangle 1 angles must be between 0 and 180 degrees.")
        return

    if angle2_a <= 0 or angle2_a >= 180 or angle2_b <= 0 or angle2_b >= 180:
        print("Triangle 2 angles must be between 0 and 180 degrees.")
        return

    if angle1_a + angle1_b >= 180:
        print("Triangle 1 has invalid angle values.")
        return

    if angle2_a + angle2_b >= 180:
        print("Triangle 2 has invalid angle values.")
        return

    if angle1_a == angle2_a and side1 == side2 and angle1_b == angle2_b:
        print("\nResult: The triangles are congruent by ASA.")
        print("Two corresponding angles and the included side are equal.")
    else:
        print("\nResult: The triangles are not proven congruent by ASA.")
        print("The required corresponding angles and included side are not all equal.")

asacongruencechecker()