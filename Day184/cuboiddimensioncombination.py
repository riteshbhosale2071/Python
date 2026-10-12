def cuboiddimensioncombination():
    print("Cuboid Dimension Combination :")

    volume = int(input("Enter the required cuboid volume: "))
    limit = int(input("Enter the maximum dimension to search: "))

    if volume <= 0 or limit <= 0:
        print("Volume and maximum dimension must be greater than zero.")
        return

    combinations = []

    for length in range(1, limit + 1):
        for width in range(length, limit + 1):
            for height in range(width, limit + 1):
                if length * width * height == volume:
                    combinations.append((length, width, height))

    print("\nDimension Combinations :")

    if len(combinations) == 0:
        print("No combinations found within the given limit.")
    else:
        for i in range(len(combinations)):
            length, width, height = combinations[i]
            print(
                i + 1,
                ". Length:", length,
                "Width:", width,
                "Height:", height,
                "Volume:", length * width * height
            )

        print("\nTotal Combinations Found:", len(combinations))

cuboiddimensioncombination()