def landdivisionarea():
    print("Land Division Area Program :")

    total_length = float(input("Enter total land length: "))
    total_width = float(input("Enter total land width: "))
    number_of_parts = int(input("Enter number of equal parts: "))

    if total_length <= 0 or total_width <= 0:
        print("Land dimensions must be greater than zero.")
        return

    if number_of_parts <= 0:
        print("Number of parts must be greater than zero.")
        return

    total_area = total_length * total_width
    area_per_part = total_area / number_of_parts

    length_per_part = total_length / number_of_parts
    width_per_part = total_width / number_of_parts

    print("\nTotal Land Area:", round(total_area, 2))
    print("Number of Parts:", number_of_parts)
    print("Area of Each Part:", round(area_per_part, 2))

    print("\nIf divided along the length:")
    print("Length of Each Part:", round(length_per_part, 2))
    print("Width of Each Part:", round(total_width, 2))

    print("\nIf divided along the width:")
    print("Length of Each Part:", round(total_length, 2))
    print("Width of Each Part:", round(width_per_part, 2))

landdivisionarea()