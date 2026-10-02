def cuboidpacking():
    print("Cuboid Packing Program :")

    container_length = float(input("Enter container length: "))
    container_width = float(input("Enter container width: "))
    container_height = float(input("Enter container height: "))

    box_length = float(input("Enter small box length: "))
    box_width = float(input("Enter small box width: "))
    box_height = float(input("Enter small box height: "))

    if (container_length <= 0 or container_width <= 0 or container_height <= 0 or
            box_length <= 0 or box_width <= 0 or box_height <= 0):
        print("All dimensions must be greater than zero.")
        return

    length_count = int(container_length // box_length)
    width_count = int(container_width // box_width)
    height_count = int(container_height // box_height)

    total_boxes = length_count * width_count * height_count

    container_volume = container_length * container_width * container_height
    box_volume = box_length * box_width * box_height
    used_volume = total_boxes * box_volume
    unused_volume = container_volume - used_volume

    print("\nBoxes Along Length:", length_count)
    print("Boxes Along Width:", width_count)
    print("Boxes Along Height:", height_count)
    print("Maximum Number of Boxes:", total_boxes)
    print("Container Volume:", round(container_volume, 2))
    print("Used Volume:", round(used_volume, 2))
    print("Unused Volume:", round(unused_volume, 2))

cuboidpacking()