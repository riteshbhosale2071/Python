def nestedrectanglearea():
    print("Nested Rectangle Area Analyzer :")

    outer_length = float(input("Enter outer rectangle length: "))
    outer_width = float(input("Enter outer rectangle width: "))
    inner_length = float(input("Enter inner rectangle length: "))
    inner_width = float(input("Enter inner rectangle width: "))

    if outer_length <= 0 or outer_width <= 0 or inner_length <= 0 or inner_width <= 0:
        print("All dimensions must be greater than zero.")
        return

    if inner_length > outer_length or inner_width > outer_width:
        print("Inner rectangle cannot be larger than the outer rectangle.")
        return

    outer_area = outer_length * outer_width
    inner_area = inner_length * inner_width
    remaining_area = outer_area - inner_area

    print("\nArea Analysis :")
    print("Outer Rectangle Area:", round(outer_area, 2))
    print("Inner Rectangle Area:", round(inner_area, 2))
    print("Remaining Area:", round(remaining_area, 2))

    if outer_area > 0:
        percentage = (inner_area / outer_area) * 100
        print("Inner Area Percentage:", round(percentage, 2), "%")
        print("Remaining Area Percentage:", round(100 - percentage, 2), "%")

    if inner_length == outer_length and inner_width == outer_width:
        print("Both rectangles have equal dimensions.")
    else:
        print("The inner rectangle is smaller than the outer rectangle.")

nestedrectanglearea()