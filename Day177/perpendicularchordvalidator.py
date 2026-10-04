def perpendicularchordvalidator():
    print("Perpendicular-Chord Validator :")

    radius = float(input("Enter radius of the circle: "))
    x1 = float(input("Enter x-coordinate of first chord endpoint: "))
    y1 = float(input("Enter y-coordinate of first chord endpoint: "))
    x2 = float(input("Enter x-coordinate of second chord endpoint: "))
    y2 = float(input("Enter y-coordinate of second chord endpoint: "))
    px = float(input("Enter x-coordinate of perpendicular point: "))
    py = float(input("Enter y-coordinate of perpendicular point: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    chord_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    if chord_length == 0:
        print("Chord endpoints cannot be the same.")
        return

    midpoint_x = (x1 + x2) / 2
    midpoint_y = (y1 + y2) / 2

    midpoint_distance = ((px - midpoint_x) ** 2 + (py - midpoint_y) ** 2) ** 0.5

    vector_x = x2 - x1
    vector_y = y2 - y1

    point_vector_x = px - midpoint_x
    point_vector_y = py - midpoint_y

    dot_product = vector_x * point_vector_x + vector_y * point_vector_y

    print("\nValidation Result :")
    print("Chord Length:", round(chord_length, 2))
    print("Chord Midpoint:", "(", round(midpoint_x, 2), ",", round(midpoint_y, 2), ")")
    print("Test Point:", "(", round(px, 2), ",", round(py, 2), ")")

    if abs(dot_product) < 0.000001:
        print("Result: The line is perpendicular to the chord.")

        if midpoint_distance < 0.000001:
            print("The perpendicular passes through the chord midpoint.")
            print("The chord is correctly bisected.")
        else:
            print("The perpendicular does not pass through the chord midpoint.")
    else:
        print("Result: The line is not perpendicular to the chord.")

perpendicularchordvalidator()