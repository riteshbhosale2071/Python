def boxcountcalculator():
    print("Box Count Calculator :")

    container_length = float(input("Enter container length: "))
    container_width = float(input("Enter container width: "))
    container_height = float(input("Enter container height: "))

    box_length = float(input("Enter box length: "))
    box_width = float(input("Enter box width: "))
    box_height = float(input("Enter box height: "))

    if (container_length <= 0 or container_width <= 0 or container_height <= 0
            or box_length <= 0 or box_width <= 0 or box_height <= 0):
        print("All dimensions must be greater than zero.")
        return

    count1 = (
        int(container_length // box_length)
        * int(container_width // box_width)
        * int(container_height // box_height)
    )

    count2 = (
        int(container_length // box_width)
        * int(container_width // box_height)
        * int(container_height // box_length)
    )

    count3 = (
        int(container_length // box_height)
        * int(container_width // box_length)
        * int(container_height // box_width)
    )

    count4 = (
        int(container_length // box_length)
        * int(container_width // box_height)
        * int(container_height // box_width)
    )

    count5 = (
        int(container_length // box_width)
        * int(container_width // box_length)
        * int(container_height // box_height)
    )

    count6 = (
        int(container_length // box_height)
        * int(container_width // box_width)
        * int(container_height // box_length)
    )

    counts = [count1, count2, count3, count4, count5, count6]
    maximum_count = max(counts)

    container_volume = container_length * container_width * container_height
    box_volume = box_length * box_width * box_height
    volume_limit = int(container_volume // box_volume)

    print("\nBox Count Results :")
    print("Container Volume:", round(container_volume, 2))
    print("Single Box Volume:", round(box_volume, 2))
    print("Best Count for Tested Orientations:", maximum_count)
    print("Volume-Based Upper Bound:", volume_limit)
    print("Unused Volume Estimate:", round(container_volume - maximum_count * box_volume, 2))

    if maximum_count == 0:
        print("The box does not fit in the container in the tested orientations.")
    else:
        print("The container can hold", maximum_count, "boxes in the best tested orientation.")

    print("Note: This calculation uses regular rows and columns without mixing orientations.")

boxcountcalculator()