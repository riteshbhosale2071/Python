def correspondingsidefinder():
    print("Corresponding Side Finder :")

    print("\nEnter side lengths of Triangle 1:")
    a1 = float(input("Side AB: "))
    b1 = float(input("Side BC: "))
    c1 = float(input("Side CA: "))

    print("\nEnter side lengths of Triangle 2:")
    a2 = float(input("Side DE: "))
    b2 = float(input("Side EF: "))
    c2 = float(input("Side FD: "))

    if a1 <= 0 or b1 <= 0 or c1 <= 0 or a2 <= 0 or b2 <= 0 or c2 <= 0:
        print("Side lengths must be positive.")
        return

    triangle1 = [a1, b1, c1]
    triangle2 = [a2, b2, c2]

    triangle1.sort()
    triangle2.sort()

    print("\nCorresponding Side Pairs:")

    if triangle1[0] == triangle2[0]:
        print("Smallest sides correspond:", triangle1[0], "=", triangle2[0])
    else:
        print("Smallest sides are not equal:", triangle1[0], "!=", triangle2[0])

    if triangle1[1] == triangle2[1]:
        print("Middle sides correspond:", triangle1[1], "=", triangle2[1])
    else:
        print("Middle sides are not equal:", triangle1[1], "!=", triangle2[1])

    if triangle1[2] == triangle2[2]:
        print("Largest sides correspond:", triangle1[2], "=", triangle2[2])
    else:
        print("Largest sides are not equal:", triangle1[2], "!=", triangle2[2])

    if triangle1 == triangle2:
        print("\nAll corresponding sides are equal.")
        print("The triangles are congruent by SSS.")
    else:
        print("\nThe corresponding side measurements are not all equal.")

correspondingsidefinder()