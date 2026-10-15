def circlearcsumchecker():
    print("Circle Arc Sum Checker :")

    number = int(input("Enter the number of arcs: "))

    if number <= 0:
        print("Number of arcs must be greater than zero.")
        return

    arcs = []
    total_angle = 0

    for i in range(number):
        print("\nArc", i + 1)
        angle = float(input("Enter central angle in degrees: "))

        if angle < 0 or angle > 360:
            print("Each angle must be between 0 and 360 degrees.")
            return

        arcs.append(angle)
        total_angle += angle

    print("\nArc Sum Analysis :")

    for i in range(number):
        print("Arc", i + 1, ":", round(arcs[i], 2), "degrees")

    print("Total Central Angle:", round(total_angle, 2), "degrees")

    if abs(total_angle - 360) < 0.000001:
        print("Result: VALID — the arcs cover exactly one full circle.")
    elif total_angle < 360:
        print("Result: INCOMPLETE — the arcs cover less than one full circle.")
        print("Missing Angle:", round(360 - total_angle, 2), "degrees")
    else:
        print("Result: EXCEEDS ONE CIRCLE — the angles sum to more than 360 degrees.")
        print("Excess Angle:", round(total_angle - 360, 2), "degrees")

    print("Percentage of Full Circle:", round(total_angle / 360 * 100, 2), "%")

circlearcsumchecker()