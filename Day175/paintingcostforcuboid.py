def paintingcostforcuboid():
    print("Painting Cost for Cuboid :")

    length = float(input("Enter cuboid length: "))
    width = float(input("Enter cuboid width: "))
    height = float(input("Enter cuboid height: "))
    cost_per_unit = float(input("Enter painting cost per square unit: "))

    if length <= 0 or width <= 0 or height <= 0 or cost_per_unit < 0:
        print("Enter valid values.")
        return

    surface_area = 2 * (length * width + width * height + height * length)
    total_cost = surface_area * cost_per_unit

    print("\nCuboid Surface Area:", round(surface_area, 2))
    print("Painting Cost per Square Unit:", round(cost_per_unit, 2))
    print("Total Painting Cost:", round(total_cost, 2))

paintingcostforcuboid()