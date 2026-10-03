def surfaceareatovolume():
    print("Surface-Area-to-Volume Comparator :")

    number_of_cuboids = int(input("Enter number of cuboids: "))

    if number_of_cuboids <= 0:
        print("Number of cuboids must be greater than zero.")
        return

    ratios = []

    for i in range(number_of_cuboids):
        print("\nCuboid", i + 1)

        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if length <= 0 or width <= 0 or height <= 0:
            print("All dimensions must be greater than zero.")
            return

        surface_area = 2 * (length * width + width * height + height * length)
        volume = length * width * height
        ratio = surface_area / volume

        ratios.append(ratio)

        print("Surface Area:", round(surface_area, 2))
        print("Volume:", round(volume, 2))
        print("Surface-Area-to-Volume Ratio:", round(ratio, 4))

    highest_ratio = max(ratios)
    lowest_ratio = min(ratios)

    print("\nComparison :")

    for i in range(number_of_cuboids):
        print("Cuboid", i + 1, "Ratio:", round(ratios[i], 4))

    print("\nHighest Ratio: Cuboid", ratios.index(highest_ratio) + 1)
    print("Lowest Ratio: Cuboid", ratios.index(lowest_ratio) + 1)

surfaceareatovolume()