def polygonareacoordinatecalc():
    print("Polygon Area Coordinate Calculator :")

    number_of_vertices = int(input("Enter number of vertices: "))

    if number_of_vertices < 3:
        print("A polygon must have at least 3 vertices.")
        return

    x = []
    y = []

    for i in range(number_of_vertices):
        print("\nVertex", i + 1)
        x_coordinate = float(input("Enter x-coordinate: "))
        y_coordinate = float(input("Enter y-coordinate: "))

        x.append(x_coordinate)
        y.append(y_coordinate)

    area = 0

    for i in range(number_of_vertices):
        next_point = (i + 1) % number_of_vertices
        area = area + (x[i] * y[next_point]) - (y[i] * x[next_point])

    area = abs(area) / 2

    print("\nResult :")
    print("Number of Vertices:", number_of_vertices)
    print("Polygon Area:", round(area, 2))

polygonareacoordinatecalc()