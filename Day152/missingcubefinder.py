def missingcubefinder():
    print("Missing Cube Finder :")

    n = int(input("Enter the number of terms: "))

    if n < 2:
        print("Enter at least 2 terms.")
        return

    terms = []

    print("\nEnter the cube sequence terms.")
    for i in range(n):
        value = int(input(f"Term {i + 1}: "))
        terms.append(value)

    print("\nCube Sequence Analysis :")
    print("Given Terms:", terms)

    roots = []

    for value in terms:
        if value >= 0:
            root = round(value ** (1 / 3))
        else:
            root = -round((-value) ** (1 / 3))

        if root ** 3 != value:
            print(f"{value} is not a perfect cube.")
            return

        roots.append(root)

    print("Cube Roots:", roots)

    differences = [
        roots[i + 1] - roots[i]
        for i in range(len(roots) - 1)
    ]

    if all(diff == differences[0] for diff in differences):
        next_root = roots[-1] + differences[0]
        missing_cube = next_root ** 3

        print("\nPattern: Constant cube-root difference")
        print("Next Cube Root:", next_root)
        print("Missing Cube:", missing_cube)
    else:
        print("\nNo consistent cube pattern detected.")

missingcubefinder()