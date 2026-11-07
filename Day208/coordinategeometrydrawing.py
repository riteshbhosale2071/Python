import matplotlib.pyplot as plt

def coordinategeometrydrawing():
    print("Coordinate Geometry Drawing Assistant")
    print("1. Plot a Single Point")
    print("2. Plot Multiple Points")
    print("3. Draw a Line")
    print("4. Draw a Triangle")
    print("5. Draw a Quadrilateral")

    choice = input("Enter your choice (1-5): ")

    try:
        plt.figure(figsize=(8, 8))

        if choice == "1":
            x = float(input("Enter x-coordinate: "))
            y = float(input("Enter y-coordinate: "))

            plt.scatter(x, y, color="red")
            plt.text(x, y, f"({x}, {y})")

        elif choice == "2":
            n = int(input("Enter number of points: "))

            if n <= 0:
                print("Number of points must be positive.")
                return

            for i in range(n):
                x = float(input(f"Enter x-coordinate of point {i + 1}: "))
                y = float(input(f"Enter y-coordinate of point {i + 1}: "))

                plt.scatter(x, y)
                plt.text(x, y, f"({x}, {y})")

        elif choice == "3":
            x1 = float(input("Enter x1: "))
            y1 = float(input("Enter y1: "))
            x2 = float(input("Enter x2: "))
            y2 = float(input("Enter y2: "))

            plt.plot([x1, x2], [y1, y2], marker="o")
            plt.text(x1, y1, f"({x1}, {y1})")
            plt.text(x2, y2, f"({x2}, {y2})")

        elif choice == "4":
            points = []

            for i in range(3):
                x = float(input(f"Enter x-coordinate of vertex {i + 1}: "))
                y = float(input(f"Enter y-coordinate of vertex {i + 1}: "))
                points.append((x, y))

            points.append(points[0])

            x_values = [p[0] for p in points]
            y_values = [p[1] for p in points]

            plt.plot(x_values, y_values, marker="o")

            for x, y in points[:-1]:
                plt.text(x, y, f"({x}, {y})")

        elif choice == "5":
            points = []

            for i in range(4):
                x = float(input(f"Enter x-coordinate of vertex {i + 1}: "))
                y = float(input(f"Enter y-coordinate of vertex {i + 1}: "))
                points.append((x, y))

            points.append(points[0])

            x_values = [p[0] for p in points]
            y_values = [p[1] for p in points]

            plt.plot(x_values, y_values, marker="o")

            for x, y in points[:-1]:
                plt.text(x, y, f"({x}, {y})")

        else:
            print("Invalid choice. Please select from 1 to 5.")
            return

        plt.axhline(0, color="black", linewidth=1)
        plt.axvline(0, color="black", linewidth=1)
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Coordinate Geometry Drawing")
        plt.grid(True)
        plt.axis("equal")
        plt.show()

    except ValueError:
        print("Please enter valid numeric coordinates.")

coordinategeometrydrawing()