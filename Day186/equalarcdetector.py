def equalarcdetector():
    print("Equal Arc Detector :")

    radius = float(input("Enter the common circle radius: "))

    if radius <= 0:
        print("Radius must be greater than zero.")
        return

    number = int(input("Enter the number of arcs to compare: "))

    if number <= 0:
        print("Number of arcs must be greater than zero.")
        return

    arcs = []

    for i in range(number):
        print("\nArc", i + 1)
        angle = float(input("Enter central angle in degrees: "))

        if angle <= 0 or angle > 360:
            print("Central angle must be greater than 0 and at most 360 degrees.")
            return

        arc_length = (angle / 360) * 2 * 3.14159 * radius
        arcs.append([i + 1, angle, arc_length])

    print("\nArc Analysis :")

    for arc in arcs:
        print(
            "Arc", arc[0],
            "- Central Angle:", round(arc[1], 2), "degrees",
            "- Arc Length:", round(arc[2], 4)
        )

    equal_found = False

    for i in range(number):
        for j in range(i + 1, number):
            if abs(arcs[i][1] - arcs[j][1]) < 0.000001:
                print(
                    "Equal Arcs Detected: Arc",
                    arcs[i][0], "and Arc", arcs[j][0]
                )
                equal_found = True

    if equal_found:
        print("\nResult: One or more pairs of equal arcs were found.")
    else:
        print("\nResult: No equal arcs were found.")

    print("Note: In the same circle, equal central angles subtend equal arcs.")

equalarcdetector()