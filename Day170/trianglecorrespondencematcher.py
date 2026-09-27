def trianglecorrespondencematcher():
    print("Triangle Correspondence Matcher :")

    print("\nEnter Triangle 1 side lengths:")
    a1 = float(input("Side AB: "))
    b1 = float(input("Side BC: "))
    c1 = float(input("Side CA: "))

    print("\nEnter Triangle 2 side lengths:")
    a2 = float(input("Side PQ: "))
    b2 = float(input("Side QR: "))
    c2 = float(input("Side RP: "))

    if a1 <= 0 or b1 <= 0 or c1 <= 0 or a2 <= 0 or b2 <= 0 or c2 <= 0:
        print("All side lengths must be positive.")
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

    print("\nSorted sides of Triangle 1:", triangle1)
    print("Sorted sides of Triangle 2:", triangle2)

    if triangle1[0] == triangle2[0] and triangle1[1] == triangle2[1] and triangle1[2] == triangle2[2]:
        print("\nResult: The triangles have matching corresponding side lengths.")
        print("Correspondence can be established by matching equal side lengths.")
    else:
        print("\nResult: The triangles do not have complete side correspondence.")
        print("Not all corresponding side lengths are equal.")

trianglecorrespondencematcher()