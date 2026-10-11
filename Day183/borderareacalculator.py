def borderareacalculator():
    print("Border Area Calculator :")

    outer_length = float(input("Enter outer rectangle length: "))
    outer_width = float(input("Enter outer rectangle width: "))
    border_width = float(input("Enter border width: "))

    if outer_length <= 0 or outer_width <= 0 or border_width <= 0:
        print("All measurements must be greater than zero.")
        return

    inner_length = outer_length - 2 * border_width
    inner_width = outer_width - 2 * border_width

    if inner_length <= 0 or inner_width <= 0:
        print("Border width is too large for the given dimensions.")
        return

    outer_area = outer_length * outer_width
    inner_area = inner_length * inner_width
    border_area = outer_area - inner_area

    print("\nBorder Area Results :")
    print("Outer Area:", round(outer_area, 2))
    print("Inner Area:", round(inner_area, 2))
    print("Border Area:", round(border_area, 2))
    print("Border Width:", border_width)

    percentage = (border_area / outer_area) * 100
    print("Percentage Covered by Border:", round(percentage, 2), "%")

borderareacalculator()