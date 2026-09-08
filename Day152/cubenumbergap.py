def cubenumbergap():
    print("Cube Number Gap Analyzer :")

    n = int(input("Enter the number of cube terms: "))

    if n < 2:
        print("Enter at least 2 terms.")
        return

    print("\nCube Number Gaps :")

    previous_cube = 0

    for i in range(1, n + 1):
        cube = i ** 3

        if i > 1:
            gap = cube - previous_cube
            print(f"Gap between {i - 1}³ and {i}³: {gap}")

        previous_cube = cube

    print("\nFormula Analysis :")
    print("The gap between consecutive cubes is:")
    print("(n + 1)³ - n³ = 3n² + 3n + 1")

cubenumbergap()