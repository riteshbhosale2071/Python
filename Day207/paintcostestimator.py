def paintcostestimator():
    print("Paint Cost Estimator")
    print("1. Calculate wall painting cost")
    print("2. Calculate room painting cost")

    choice = input("Enter your choice (1 or 2): ")

    try:
        if choice == "1":
            length = float(input("Enter wall length (meters): "))
            height = float(input("Enter wall height (meters): "))
            paint_rate = float(input("Enter paint cost per square meter: "))
            coats = int(input("Enter number of paint coats: "))

            if length <= 0 or height <= 0 or paint_rate <= 0 or coats <= 0:
                print("All values must be greater than zero.")
                return

            area = length * height
            total_area = area * coats
            cost = total_area * paint_rate

        elif choice == "2":
            length = float(input("Enter room length (meters): "))
            breadth = float(input("Enter room breadth (meters): "))
            height = float(input("Enter room height (meters): "))
            paint_rate = float(input("Enter paint cost per square meter: "))
            coats = int(input("Enter number of paint coats: "))

            if length <= 0 or breadth <= 0 or height <= 0 or paint_rate <= 0 or coats <= 0:
                print("All values must be greater than zero.")
                return

            area = 2 * height * (length + breadth)
            total_area = area * coats
            cost = total_area * paint_rate

        else:
            print("Invalid choice. Please select 1 or 2.")
            return

        print("\nPaint Cost Details")
        print("Total Wall Area:", round(area, 2), "square meters")
        print("Area for All Coats:", round(total_area, 2), "square meters")
        print("Estimated Paint Cost: Rs.", round(cost, 2))

    except ValueError:
        print("Please enter valid numeric values.")

paintcostestimator()