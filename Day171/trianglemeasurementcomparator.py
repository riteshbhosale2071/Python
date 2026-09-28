def trianglemeasurementcomparator():
    print("Triangle Measurement Comparator :")

    print("\nEnter measurements of Triangle 1:")
    side1_a = float(input("Side 1: "))
    side1_b = float(input("Side 2: "))
    side1_c = float(input("Side 3: "))

    print("\nEnter measurements of Triangle 2:")
    side2_a = float(input("Side 1: "))
    side2_b = float(input("Side 2: "))
    side2_c = float(input("Side 3: "))

    if side1_a <= 0 or side1_b <= 0 or side1_c <= 0 or side2_a <= 0 or side2_b <= 0 or side2_c <= 0:
        print("All side lengths must be positive.")
        return

    triangle1 = [side1_a, side1_b, side1_c]
    triangle2 = [side2_a, side2_b, side2_c]

    triangle1.sort()
    triangle2.sort()

    print("\nTriangle 1 Measurements:", triangle1)
    print("Triangle 2 Measurements:", triangle2)

    if triangle1[0] == triangle2[0] and triangle1[1] == triangle2[1] and triangle1[2] == triangle2[2]:
        print("\nResult: Both triangles have the same measurements.")
        print("The triangles are congruent by SSS.")
    elif triangle1[0] == triangle2[0] and triangle1[1] == triangle2[1]:
        print("\nResult: Two corresponding measurements are equal.")
        print("The triangles are not proven congruent by SSS.")
    else:
        print("\nResult: The triangle measurements are different.")
        print("The triangles are not congruent by SSS.")

trianglemeasurementcomparator()