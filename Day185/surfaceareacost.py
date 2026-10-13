def surfaceareacost():
    print("Surface Area Cost Calculator :")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")

    choice = input("Select a shape (1-3): ")

    if choice == "1":
        side = float(input("Enter cube side length: "))

        if side <= 0:
            print("Side length must be greater than zero.")
            return

        surface_area = 6 * side * side
        shape = "Cube"

    elif choice == "2":
        length = float(input("Enter cuboid length: "))
        width = float(input("Enter cuboid width: "))
        height = float(input("Enter cuboid height: "))

        if length <= 0 or width <= 0 or height <= 0:
            print("All dimensions must be greater than zero.")
            return

        surface_area = 2 * (
            length * width + width * height + length * height
        )
        shape = "Cuboid"

    elif choice == "3":
        radius = float(input("Enter cylinder radius: "))
        height = float(input("Enter cylinder height: "))

        if radius <= 0 or height <= 0:
            print("Radius and height must be greater than zero.")
            return

        surface_area = 2 * 3.14159 * radius * (radius + height)
        shape = "Cylinder"

    else:
        print("Invalid selection. Choose 1, 2, or 3.")
        return

    cost_per_unit = float(input("Enter cost per square unit: "))

    if cost_per_unit < 0:
        print("Cost cannot be negative.")
        return

    total_cost = surface_area * cost_per_unit

    print("\nCost Calculation Results :")
    print("Shape:", shape)
    print("Surface Area:", round(surface_area, 2), "square units")
    print("Cost per Square Unit:", round(cost_per_unit, 2))
    print("Total Surface Area Cost:", round(total_cost, 2))

    if total_cost == 0:
        print("No cost is required.")
    else:
        print("Estimated total cost:", round(total_cost, 2))

surfaceareacost()