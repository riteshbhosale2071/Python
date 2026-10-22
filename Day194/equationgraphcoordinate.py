def equationgraphcoordinate():
    print("Equation Graph Coordinate :")
    print("Equation format: y = ax + b")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter constant b: "))
        start_x = int(input("Enter starting x-coordinate: "))
        end_x = int(input("Enter ending x-coordinate: "))
        step = int(input("Enter step size: "))
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")
        return

    if step <= 0:
        print("Step size must be greater than zero.")
        return

    if start_x > end_x:
        print("Starting x-coordinate must not exceed ending x-coordinate.")
        return

    coordinates = []

    print("\nGenerated Coordinates :")
    print("Equation: y =", a, "x +", b)
    print("{:<12}{:<12}".format("X-coordinate", "Y-coordinate"))
    print("-" * 24)

    x = start_x

    while x <= end_x:
        y = a * x + b
        coordinates.append((x, y))
        print("{:<12}{:<12}".format(x, round(y, 4)))
        x += step

    print("\nCoordinate Summary :")
    print("Total Coordinates Generated:", len(coordinates))

    if coordinates:
        print("First Coordinate:", coordinates[0])
        print("Last Coordinate:", coordinates[-1])

        y_values = [point[1] for point in coordinates]
        print("Minimum Y-value:", min(y_values))
        print("Maximum Y-value:", max(y_values))

    print("\nGraph Plotting Data :")

    for x, y in coordinates:
        print("(" + str(x) + ", " + str(round(y, 4)) + ")")

    print("\nUse these coordinate pairs to plot the equation on a graph.")

equationgraphcoordinate()