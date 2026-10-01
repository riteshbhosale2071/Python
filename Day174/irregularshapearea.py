def irregularshapearea():
    print("Irregular Shape Area Estimator :")

    number_of_sections = int(input("Enter number of sections: "))

    if number_of_sections <= 0:
        print("Number of sections must be greater than zero.")
        return

    total_area = 0

    for i in range(number_of_sections):
        print("\nSection", i + 1)
        print("1. Rectangle")
        print("2. Triangle")
        print("3. Trapezium")

        choice = int(input("Enter section type: "))

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

        else:
            print("Invalid section type.")
            return

        total_area += area
        print("Section Area:", round(area, 2))

    print("\nResult :")
    print("Estimated Irregular Shape Area:", round(total_area, 2))

irregularshapearea()