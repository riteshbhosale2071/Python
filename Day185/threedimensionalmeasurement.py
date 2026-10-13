def threedimensionalmeasurement():
    print("Three-Dimensional Measurement Validator :")
    print("1. Cube")
    print("2. Cuboid")
    print("3. Cylinder")
    print("4. Sphere")

    choice = input("Select a shape (1-4): ")

    if choice == "1":
        side = float(input("Enter cube side length: "))

        if side <= 0:
            print("Invalid measurement: Side length must be positive.")
            return

        volume = side ** 3
        surface_area = 6 * side ** 2
        shape = "Cube"

    elif choice == "2":
        length = float(input("Enter cuboid length: "))
        width = float(input("Enter cuboid width: "))
        height = float(input("Enter cuboid height: "))

        if length <= 0 or width <= 0 or height <= 0:
            print("Invalid measurements: All dimensions must be positive.")
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
            print("Invalid measurements: Radius and height must be positive.")
            return

        volume = 3.14159 * radius ** 2 * height
        surface_area = 2 * 3.14159 * radius * (radius + height)
        shape = "Cylinder"

    elif choice == "4":
        radius = float(input("Enter sphere radius: "))

        if radius <= 0:
            print("Invalid measurement: Radius must be positive.")
            return

        volume = (4 / 3) * 3.14159 * radius ** 3
        surface_area = 4 * 3.14159 * radius ** 2
        shape = "Sphere"

    else:
        print("Invalid selection. Choose a number from 1 to 4.")
        return

    print("\nMeasurement Validation Report :")
    print("Shape:", shape)
    print("Validation Status: PASSED")
    print("Volume:", round(volume, 2), "cubic units")
    print("Surface Area:", round(surface_area, 2), "square units")

    if volume > 0 and surface_area > 0:
        ratio = volume / surface_area
        print("Volume-to-Surface Ratio:", round(ratio, 4))
        print("Ratio Validation: PASSED")
    else:
        print("Calculation validation failed.")

    print("All entered dimensions are valid positive values.")

threedimensionalmeasurement()