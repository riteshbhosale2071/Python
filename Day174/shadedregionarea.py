def shadedregionarea():
    print("Shaded Region Area Calculator :")

    print("\nChoose the outer shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    outer_shape = int(input("Enter choice: "))

    if outer_shape == 1:
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        if length <= 0 or width <= 0:
            print("Invalid dimensions.")
            return

        outer_area = length * width

    elif outer_shape == 2:
        radius = float(input("Enter circle radius: "))

        if radius <= 0:
            print("Invalid radius.")
            return

        outer_area = 3.14159 * radius * radius

    elif outer_shape == 3:
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))

        if base <= 0 or height <= 0:
            print("Invalid dimensions.")
            return

        outer_area = 0.5 * base * height

    else:
        print("Invalid outer shape.")
        return

    print("\nChoose the inner unshaded shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    inner_shape = int(input("Enter choice: "))

    if inner_shape == 1:
        length = float(input("Enter inner rectangle length: "))
        width = float(input("Enter inner rectangle width: "))

        if length <= 0 or width <= 0:
            print("Invalid dimensions.")
            return

        inner_area = length * width

    elif inner_shape == 2:
        radius = float(input("Enter inner circle radius: "))

        if radius <= 0:
            print("Invalid radius.")
            return

        inner_area = 3.14159 * radius * radius

    elif inner_shape == 3:
        base = float(input("Enter inner triangle base: "))
        height = float(input("Enter inner triangle height: "))

        if base <= 0 or height <= 0:
            print("Invalid dimensions.")
            return

        inner_area = 0.5 * base * height

    else:
        print("Invalid inner shape.")
        return

    if inner_area > outer_area:
        print("Inner area cannot be greater than outer area.")
        return

    shaded_area = outer_area - inner_area

    print("\nOuter Area:", round(outer_area, 2))
    print("Unshaded Area:", round(inner_area, 2))
    print("Shaded Region Area:", round(shaded_area, 2))

shadedregionarea()