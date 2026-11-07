import math

def constructiondatavalidator():
    print("Construction Data Validator")

    try:
        project_name = input("Enter project name: ").strip()
        if not project_name:
            print("Error: Project name cannot be empty.")
            return

        length = float(input("Enter construction length (meters): "))
        width = float(input("Enter construction width (meters): "))
        floors = int(input("Enter number of floors: "))
        workers = int(input("Enter number of workers: "))
        cement = float(input("Enter cement quantity (bags): "))
        steel = float(input("Enter steel quantity (kg): "))
        budget = float(input("Enter project budget (₹): "))

        errors = []

        if length <= 0:
            errors.append("Length must be greater than zero.")

        if width <= 0:
            errors.append("Width must be greater than zero.")

        if floors <= 0:
            errors.append("Number of floors must be at least one.")

        if workers <= 0:
            errors.append("Number of workers must be at least one.")

        if cement < 0:
            errors.append("Cement quantity cannot be negative.")

        if steel < 0:
            errors.append("Steel quantity cannot be negative.")

        if budget <= 0:
            errors.append("Budget must be greater than zero.")

        if errors:
            print("\nValidation Failed!")
            for error in errors:
                print("-", error)
            return

        area = length * width
        total_area = area * floors

        print("\nConstruction Data Report")
        print("Project Name:", project_name)
        print("Floor Area:", round(area, 2), "sq. meters")
        print("Total Construction Area:", round(total_area, 2), "sq. meters")
        print("Number of Floors:", floors)
        print("Number of Workers:", workers)
        print("Cement Quantity:", cement, "bags")
        print("Steel Quantity:", steel, "kg")
        print("Project Budget: ₹", round(budget, 2))

        print("\nValidation Status: All entered data is valid.")
        print("Construction data successfully verified.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

constructiondatavalidator()