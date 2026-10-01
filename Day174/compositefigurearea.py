def compositefigurearea():
    print("Composite Figure Area Calculator :")

    number_of_shapes = int(input("Enter number of shapes: "))

    if number_of_shapes <= 0:
        print("Number of shapes must be greater than zero.")
        return

    total_area = 0

    for i in range(number_of_shapes):
        print("\nShape", i + 1)
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Trapezium")
        print("4. Circle")

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
            side1 = float(input("Enter first parallel side: "))
            side2 = float(input("Enter second parallel side: "))
            height = float(input("Enter height: "))

            if side1 <= 0 or side2 <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            area = 0.5 * (side1 + side2) * height

        elif choice == 4:
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Invalid radius.")
                return

            area = 3.14159 * radius * radius

        else:
            print("Invalid shape type.")
            return

        print("Area of Shape", i + 1, ":", round(area, 2))
        total_area += area

    print("\nTotal Composite Figure Area:", round(total_area, 2))

compositefigurearea()