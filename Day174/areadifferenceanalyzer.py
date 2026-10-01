def areadifferenceanalyzer():
    print("Area Difference Analyzer :")

    number_of_shapes = int(input("Enter number of shapes to compare: "))

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

        elif choice == 2:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            area = 0.5 * base * height

        elif choice == 3:
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Invalid radius.")
                return

            area = 3.14159 * radius * radius

        elif choice == 4:
            side1 = float(input("Enter first parallel side: "))
            side2 = float(input("Enter second parallel side: "))
            height = float(input("Enter height: "))

            if side1 <= 0 or side2 <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            area = 0.5 * (side1 + side2) * height

        else:
            print("Invalid shape type.")
            return

        areas.append(area)
        print("Area of Shape", i + 1, ":", round(area, 2))

    largest_area = max(areas)
    smallest_area = min(areas)
    difference = largest_area - smallest_area

    print("\nArea Difference :")
    print("Largest Area:", round(largest_area, 2))
    print("Smallest Area:", round(smallest_area, 2))
    print("Difference:", round(difference, 2))

areadifferenceanalyzer()