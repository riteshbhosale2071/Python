def openboxmaterial():
    print("Open-Box Material Calculator :")

    length = float(input("Enter box length: "))
    width = float(input("Enter box width: "))
    height = float(input("Enter box height: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("All dimensions must be greater than zero.")
        return

    bottom_area = length * width
    front_back_area = 2 * length * height
    left_right_area = 2 * width * height

    total_material_area = bottom_area + front_back_area + left_right_area

    print("\nOpen-Box Material Details :")
    print("Bottom Area:", round(bottom_area, 2), "square units")
    print("Front and Back Area:", round(front_back_area, 2), "square units")
    print("Left and Right Area:", round(left_right_area, 2), "square units")
    print("Total Material Area:", round(total_material_area, 2), "square units")

    cost_per_unit = float(input("Enter material cost per square unit: "))

    if cost_per_unit < 0:
        print("Material cost cannot be negative.")
        return

    wastage_percentage = float(input("Enter additional material wastage percentage: "))

    if wastage_percentage < 0:
        print("Wastage percentage cannot be negative.")
        return

    wastage_area = total_material_area * wastage_percentage / 100
    required_material = total_material_area + wastage_area
    total_cost = required_material * cost_per_unit

    print("\nFinal Material Report :")
    print("Base Material Required:", round(total_material_area, 2), "square units")
    print("Extra Material for Wastage:", round(wastage_area, 2), "square units")
    print("Total Material Required:", round(required_material, 2), "square units")
    print("Total Material Cost:", round(total_cost, 2))

openboxmaterial()