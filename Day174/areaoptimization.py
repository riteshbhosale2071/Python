def areaoptimization():
    print("Area Optimization Problem :")

    perimeter = float(input("Enter fixed perimeter: "))

    if perimeter <= 0:
        print("Perimeter must be greater than zero.")
        return

    best_length = 0
    best_width = 0
    best_area = 0

    length = 0.1

    while length < perimeter / 2:
        width = (perimeter - 2 * length) / 2
        area = length * width

        if width > 0 and area > best_area:
            best_area = area
            best_length = length
            best_width = width

        length += 0.1

    print("\nFixed Perimeter:", round(perimeter, 2))
    print("Best Length:", round(best_length, 2))
    print("Best Width:", round(best_width, 2))
    print("Maximum Area:", round(best_area, 2))

areaoptimization()