def volumetosurfaceratio():
    print("Volume-to-Surface Ratio :")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Sphere")

    choice = input("Select a shape (1-4): ")

    if choice == "1":
        side = float(input("Enter cube side length: "))

        if side <= 0:
            print("Side length must be greater than zero.")
            return

        volume = side ** 3
        surface_area = 6 * side ** 2
        shape = "Cube"

    elif choice == "2":
        length = float(input("Enter cuboid length: "))
        width = float(input("Enter cuboid width: "))
        height = float(input("Enter cuboid height: "))

        if length <= 0 or width <= 0 or height <= 0:
            print("All dimensions must be greater than zero.")
            return

        volume = length * width * height
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

        volume = 3.14159 * radius ** 2 * height
        surface_area = 2 * 3.14159 * radius * (radius + height)
        shape = "Cylinder"

    elif choice == "4":
        radius = float(input("Enter sphere radius: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        volume = (4 / 3) * 3.14159 * radius ** 3
        surface_area = 4 * 3.14159 * radius ** 2
        shape = "Sphere"

    else:
        print("Invalid selection. Choose a number from 1 to 4.")
        return

    ratio = volume / surface_area

    print("\nCalculation Results :")
    print("Shape:", shape)
    print("Volume:", round(volume, 2), "cubic units")
    print("Surface Area:", round(surface_area, 2), "square units")
    print("Volume-to-Surface Ratio:", round(ratio, 4))
    print("Ratio Percentage:", round(ratio * 100, 2), "%")

    if ratio > 1:
        print("Result: Volume is numerically greater than surface area.")
    elif ratio < 1:
        print("Result: Surface area is numerically greater than volume.")
    else:
        print("Result: Volume and surface area have equal numerical values.")

    print("Note: The ratio has units of length.")

volumetosurfaceratio()