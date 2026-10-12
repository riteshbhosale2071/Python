def tankcapacitycomparison():
    print("Tank Capacity Comparison :")

    number = int(input("Enter the number of tanks to compare: "))

    if number <= 0:
        print("Number of tanks must be greater than zero.")
        return

    tanks = []

    for i in range(number):
        print("\nTank", i + 1)

        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if length <= 0 or width <= 0 or height <= 0:
            print("All dimensions must be greater than zero.")
            return

        capacity = length * width * height
        tanks.append([i + 1, capacity])

        print("Tank Capacity:", round(capacity, 2), "cubic units")
        print("Capacity in Liters:", round(capacity / 1000, 2), "liters")

    tanks.sort(key=lambda tank: tank[1], reverse=True)

    print("\nTank Capacity Ranking :")

    for i in range(number):
        print(
            "Rank", i + 1,
            "- Tank", tanks[i][0],
            "- Capacity:", round(tanks[i][1], 2),
            "cubic units"
        )

    largest = tanks[0]
    smallest = tanks[-1]

    print("\nLargest Tank: Tank", largest[0])
    print("Largest Capacity:", round(largest[1], 2), "cubic units")

    print("\nSmallest Tank: Tank", smallest[0])
    print("Smallest Capacity:", round(smallest[1], 2), "cubic units")

    difference = largest[1] - smallest[1]
    print("\nCapacity Difference:", round(difference, 2), "cubic units")

    if smallest[1] > 0:
        ratio = largest[1] / smallest[1]
        print("Largest-to-Smallest Capacity Ratio:", round(ratio, 2))

tankcapacitycomparison()