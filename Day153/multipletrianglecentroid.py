def multipletrianglecentroid():
    print("Multiple Triangle Centroid Analyzer :")

    n = int(input("Enter number of triangles: "))

    if n <= 0:
        print("Number of triangles must be positive.")
        return

    centroids = []

    for i in range(1, n + 1):
        print(f"\nTriangle {i} :")

        x1 = float(input("Enter A x-coordinate: "))
        y1 = float(input("Enter A y-coordinate: "))

        x2 = float(input("Enter B x-coordinate: "))
        y2 = float(input("Enter B y-coordinate: "))

        x3 = float(input("Enter C x-coordinate: "))
        y3 = float(input("Enter C y-coordinate: "))

        cx = (x1 + x2 + x3) / 3
        cy = (y1 + y2 + y3) / 3

        centroids.append((cx, cy))

        print(f"Centroid of Triangle {i}: ({cx:.2f}, {cy:.2f})")

    print("\nCentroid Summary :")

    for i, (cx, cy) in enumerate(centroids, start=1):
        print(f"Triangle {i}: ({cx:.2f}, {cy:.2f})")

    average_x = sum(cx for cx, cy in centroids) / n
    average_y = sum(cy for cx, cy in centroids) / n

    print("\nOverall Analysis :")
    print(f"Average Centroid Position: ({average_x:.2f}, {average_y:.2f})")

multipletrianglecentroid()