def multishapearea():
    print("Multi-Shape Area Report :")

    number_of_shapes = int(input("Enter number of shapes: "))

    if number_of_shapes <= 0:
        print("Number of shapes must be greater than zero.")
        return

    areas = []

    for i in range(number_of_shapes):
        print("\nShape", i + 1)
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Circle")
        print("4. Trapezium")

        choice = int(input("Enter shape type: "))

        if choice == 1:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length <= 0 or width <= 0:
                print("Invalid dimensions.")
                return

            area = length * width
            shape_name = "Rectangle"

        elif choice == 2:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            area = 0.5 * base * height
            shape_name = "Triangle"

        elif choice == 3:
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Invalid radius.")
                return

            area = 3.14159 * radius * radius
            shape_name = "Circle"

        elif choice == 4:
            side1 = float(input("Enter first parallel side: "))
            side2 = float(input("Enter second parallel side: "))
            height = float(input("Enter height: "))

            if side1 <= 0 or side2 <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            area = 0.5 * (side1 + side2) * height
            shape_name = "Trapezium"

        else:
            print("Invalid shape type.")
            return

        areas.append(area)

        print("Shape:", shape_name)
        print("Area:", round(area, 2))

    total_area = sum(areas)
    largest_area = max(areas)
    smallest_area = min(areas)

    print("\nMulti-Shape Area Report :")
    print("Total Area:", round(total_area, 2))
    print("Largest Area:", round(largest_area, 2))
    print("Smallest Area:", round(smallest_area, 2))
    print("Average Area:", round(total_area / number_of_shapes, 2))

    for i in range(number_of_shapes):
        percentage = (areas[i] / total_area) * 100
        print("Shape", i + 1, "Contribution:", round(percentage, 2), "%")

multishapearea()