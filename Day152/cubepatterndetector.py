def cubepatterndetector():
    print("Cube Pattern Detector :")

    n = int(input("Enter number of terms: "))

    if n < 2:
        print("Enter at least 2 terms.")
        return

    terms = []

    for i in range(n):
        value = int(input(f"Enter term {i + 1}: "))
        terms.append(value)

    print("\nCube Pattern Analysis :")
    print("Sequence:", terms)

    cube_roots = []
    all_cubes = True

    for value in terms:
        if value >= 0:
            root = round(value ** (1 / 3))
        else:
            root = -round((-value) ** (1 / 3))

        while (root + 1) ** 3 <= value:
            root += 1

        while root ** 3 > value:
            root -= 1

        if root ** 3 == value:
            cube_roots.append(root)
        else:
            all_cubes = False
            break

    if all_cubes:
        print("All terms are perfect cubes.")
        print("Cube roots:", cube_roots)

        if all(
            cube_roots[i] == cube_roots[0] + i
            for i in range(len(cube_roots))
        ):
            print("Pattern detected: Consecutive cube numbers.")
        else:
            print("Pattern detected: Perfect cubes, but roots are not consecutive.")
    else:
        print("The sequence does not consist entirely of perfect cubes.")

cubepatterndetector()