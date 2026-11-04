def cartesianpointplotdata():
    count = int(input("Enter the number of points to generate: "))

    if count <= 0:
        print("Invalid number. Enter a positive integer.")
        return

    points = []

    for i in range(count):
        print(f"\nPoint {i + 1}")
        x = float(input("Enter X-coordinate: "))
        y = float(input("Enter Y-coordinate: "))
        points.append((x, y))

    print("\nCartesian Point Plot Data :")
    print("Point\tX-coordinate\tY-coordinate")

    for i, (x, y) in enumerate(points, start=1):
        print(f"P{i}\t{x:.2f}\t\t{y:.2f}")

    print("\nPlot Data:")
    print("[" + ", ".join(f"({x:.2f}, {y:.2f})" for x, y in points) + "]")

cartesianpointplotdata()