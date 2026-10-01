def areapartition():
    print("Area Partition Simulator :")

    total_area = float(input("Enter total area: "))
    number_of_parts = int(input("Enter number of parts: "))

    if total_area <= 0 or number_of_parts <= 0:
        print("Enter valid values.")
        return

    areas = []
    remaining_area = total_area

    for i in range(number_of_parts):
        if i == number_of_parts - 1:
            part_area = remaining_area
        else:
            part_area = float(input("Enter area of part " + str(i + 1) + ": "))

            if part_area <= 0 or part_area > remaining_area:
                print("Invalid part area.")
                return

        areas.append(part_area)
        remaining_area = remaining_area - part_area

    print("\nArea Partition Result :")

    for i in range(number_of_parts):
        percentage = (areas[i] / total_area) * 100
        print("Part", i + 1, "Area:", round(areas[i], 2))
        print("Part", i + 1, "Percentage:", round(percentage, 2), "%")

    print("\nTotal Partitioned Area:", round(sum(areas), 2))
    print("Remaining Area:", round(remaining_area, 2))

areapartition()