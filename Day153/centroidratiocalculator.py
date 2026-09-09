def centroidratiocalculator():
    print("Centroid Ratio Calculator :")

    median = float(input("Enter the length of the median: "))

    if median <= 0:
        print("Median length must be positive.")
        return

    vertex_to_centroid = (2 / 3) * median
    centroid_to_midpoint = (1 / 3) * median

    print("\nCentroid Ratio :")
    print("Median Length:", median)
    print("Vertex to Centroid:", vertex_to_centroid)
    print("Centroid to Midpoint:", centroid_to_midpoint)

    print("\nRatio:")
    print("Vertex : Centroid : Midpoint = 2 : 1")

    print("\nVerification:")
    print(
        f"{vertex_to_centroid:.2f} : "
        f"{centroid_to_midpoint:.2f} = 2 : 1"
    )

centroidratiocalculator()