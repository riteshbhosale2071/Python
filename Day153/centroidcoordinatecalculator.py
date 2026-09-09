def centroidcoordinatecalculator():
    print("Centroid Coordinate Calculator :")

    print("\nEnter coordinates of Vertex A:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))

    print("\nEnter coordinates of Vertex B:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    print("\nEnter coordinates of Vertex C:")
    x3 = float(input("x3: "))
    y3 = float(input("y3: "))

    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3

    print("\nCentroid Coordinates :")
    print("Vertex A:", (x1, y1))
    print("Vertex B:", (x2, y2))
    print("Vertex C:", (x3, y3))

    print("\nCentroid:")
    print(f"G = ({centroid_x:.2f}, {centroid_y:.2f})")

centroidcoordinatecalculator()