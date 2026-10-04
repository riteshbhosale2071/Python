def circlearccomparison():
    print("Circle Arc Comparison Engine :")

    radius = float(input("Enter radius of the circle: "))
    number_of_arcs = int(input("Enter number of arcs: "))

    if radius <= 0 or number_of_arcs <= 0:
        print("Enter valid values.")
        return

    pi = 3.14159
    arcs = []

    for i in range(number_of_arcs):
        angle = float(input("Enter central angle of arc " + str(i + 1) + " in degrees: "))

        if angle <= 0 or angle > 360:
            print("Angle must be between 0 and 360 degrees.")
            return

        arc_length = (angle / 360) * 2 * pi * radius
        arcs.append([i + 1, angle, arc_length])

    print("\nArc Comparison :")

    for arc in arcs:
        print("Arc", arc[0], "- Angle:", round(arc[1], 2), "degrees - Length:", round(arc[2], 2))

    longest = max(arcs, key=lambda x: x[2])
    shortest = min(arcs, key=lambda x: x[2])

    print("\nLongest Arc:")
    print("Arc", longest[0], "with length", round(longest[2], 2))

    print("\nShortest Arc:")
    print("Arc", shortest[0], "with length", round(shortest[2], 2))

    if abs(longest[2] - shortest[2]) < 0.000001:
        print("\nAll arcs have equal lengths.")
    else:
        print("\nThe arcs have different lengths.")

circlearccomparison()