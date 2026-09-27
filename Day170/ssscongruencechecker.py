def ssscongruencechecker():
    print("SSS Congruence Checker :")

    print("\nEnter side lengths of Triangle 1:")
    a1 = float(input("Side 1: "))
    b1 = float(input("Side 2: "))
    c1 = float(input("Side 3: "))

    print("\nEnter side lengths of Triangle 2:")
    a2 = float(input("Side 1: "))
    b2 = float(input("Side 2: "))
    c2 = float(input("Side 3: "))

    if a1 <= 0 or b1 <= 0 or c1 <= 0 or a2 <= 0 or b2 <= 0 or c2 <= 0:
        print("Side lengths must be positive.")
        return

    if a1 + b1 <= c1 or a1 + c1 <= b1 or b1 + c1 <= a1:
        print("Triangle 1 is invalid.")
        return

    if a2 + b2 <= c2 or a2 + c2 <= b2 or b2 + c2 <= a2:
        print("Triangle 2 is invalid.")
        return

    triangle1 = [a1, b1, c1]
    triangle2 = [a2, b2, c2]

    triangle1.sort()
    triangle2.sort()

    print("\nSorted Sides of Triangle 1:", triangle1)
    print("Sorted Sides of Triangle 2:", triangle2)

    if triangle1[0] == triangle2[0] and triangle1[1] == triangle2[1] and triangle1[2] == triangle2[2]:
        print("\nResult: The triangles are congruent by SSS.")
        print("All three corresponding side lengths are equal.")
    else:
        print("\nResult: The triangles are not congruent by SSS.")
        print("All three corresponding side lengths are not equal.")

ssscongruencechecker()