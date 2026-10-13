def cubesurfaceareacomparison():
    print("Cube Surface Area Comparison :")

    number = int(input("Enter the number of cubes to compare: "))

    if number <= 0:
        print("Number of cubes must be greater than zero.")
        return

    cubes = []

    for i in range(number):
        print("\nCube", i + 1)
        side = float(input("Enter cube side length: "))

        if side <= 0:
            print("Side length must be greater than zero.")
            return

        surface_area = 6 * side * side
        volume = side ** 3

        cubes.append([i + 1, side, surface_area, volume])

    cubes.sort(key=lambda cube: cube[2], reverse=True)

    print("\nSurface Area Comparison Report :")

    for i in range(number):
        cube = cubes[i]
        print("\nRank:", i + 1)
        print("Cube Number:", cube[0])
        print("Side Length:", round(cube[1], 2))
        print("Surface Area:", round(cube[2], 2), "square units")
        print("Volume:", round(cube[3], 2), "cubic units")

    largest = cubes[0]
    smallest = cubes[-1]

    print("\nFinal Comparison :")
    print("Largest Surface Area: Cube", largest[0])
    print("Largest Area:", round(largest[2], 2), "square units")
    print("Smallest Surface Area: Cube", smallest[0])
    print("Smallest Area:", round(smallest[2], 2), "square units")
    print("Surface Area Difference:", round(largest[2] - smallest[2], 2))

    if smallest[2] > 0:
        print("Surface Area Ratio:", round(largest[2] / smallest[2], 2))

cubesurfaceareacomparison()