def cubenumbersearchengine():
    print("Cube Number Search Engine :")

    start = int(input("Enter starting number: "))
    end = int(input("Enter ending number: "))

    if start > end:
        print("Starting number must be less than or equal to ending number.")
        return

    cube_numbers = []

    for number in range(start, end + 1):
        if number >= 0:
            root = round(number ** (1 / 3))
        else:
            root = -round((-number) ** (1 / 3))

        while (root + 1) ** 3 <= number:
            root += 1

        while root ** 3 > number:
            root -= 1

        if root ** 3 == number:
            cube_numbers.append((number, root))

    print("\nCube Number Search Results :")

    if cube_numbers:
        print("Perfect cubes found:")

        for number, root in cube_numbers:
            print(f"{number} = {root}³")

        print("\nTotal Perfect Cubes:", len(cube_numbers))
    else:
        print("No perfect cube numbers found in the given range.")

cubenumbersearchengine()