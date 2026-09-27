def sascongruencechecker():
    print("SAS Congruence Checker :")

    print("\nEnter Triangle 1:")
    side1_a = float(input("Enter first side: "))
    angle1 = float(input("Enter included angle: "))
    side1_b = float(input("Enter second side: "))

    print("\nEnter Triangle 2:")
    side2_a = float(input("Enter first side: "))
    angle2 = float(input("Enter included angle: "))
    side2_b = float(input("Enter second side: "))

    if side1_a <= 0 or side1_b <= 0 or side2_a <= 0 or side2_b <= 0:
        print("Side lengths must be positive.")
        return

    if angle1 <= 0 or angle1 >= 180 or angle2 <= 0 or angle2 >= 180:
        print("Angles must be between 0 and 180 degrees.")
        return

    if side1_a == side2_a and side1_b == side2_b and angle1 == angle2:
        print("\nResult: The triangles are congruent by SAS.")
        print("Two corresponding sides and the included angle are equal.")
    else:
        print("\nResult: The triangles are not proven congruent by SAS.")
        print("The required corresponding sides and included angle are not all equal.")

sascongruencechecker()