def correspondinganglefinder():
    print("Corresponding Angle Finder :")

    print("\nEnter angles of Triangle 1:")
    angle1_a = float(input("Angle A: "))
    angle1_b = float(input("Angle B: "))
    angle1_c = float(input("Angle C: "))

    print("\nEnter angles of Triangle 2:")
    angle2_a = float(input("Angle D: "))
    angle2_b = float(input("Angle E: "))
    angle2_c = float(input("Angle F: "))

    if angle1_a <= 0 or angle1_b <= 0 or angle1_c <= 0:
        print("Triangle 1 angles must be positive.")
        return

    if angle2_a <= 0 or angle2_b <= 0 or angle2_c <= 0:
        print("Triangle 2 angles must be positive.")
        return

    if angle1_a + angle1_b + angle1_c != 180:
        print("Triangle 1 has invalid angles.")
        return

    if angle2_a + angle2_b + angle2_c != 180:
        print("Triangle 2 has invalid angles.")
        return

    triangle1 = [angle1_a, angle1_b, angle1_c]
    triangle2 = [angle2_a, angle2_b, angle2_c]

    triangle1.sort()
    triangle2.sort()

    print("\nCorresponding Angle Pairs:")

    if triangle1[0] == triangle2[0]:
        print("Smallest angles correspond:", triangle1[0], "=", triangle2[0])
    else:
        print("Smallest angles are not equal:", triangle1[0], "!=", triangle2[0])

    if triangle1[1] == triangle2[1]:
        print("Middle angles correspond:", triangle1[1], "=", triangle2[1])
    else:
        print("Middle angles are not equal:", triangle1[1], "!=", triangle2[1])

    if triangle1[2] == triangle2[2]:
        print("Largest angles correspond:", triangle1[2], "=", triangle2[2])
    else:
        print("Largest angles are not equal:", triangle1[2], "!=", triangle2[2])

    if triangle1 == triangle2:
        print("\nAll corresponding angles are equal.")
        print("The triangles are similar by AAA.")
    else:
        print("\nThe corresponding angle measurements are not all equal.")

correspondinganglefinder()