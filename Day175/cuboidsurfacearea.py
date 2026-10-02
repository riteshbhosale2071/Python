def cuboidsurfacearea():
    print("Cuboid Surface Area Calculator :")

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("All dimensions must be greater than zero.")
        return

    lateral_surface_area = 2 * height * (length + width)
    total_surface_area = 2 * (length * width + width * height + height * length)

    print("\nLength:", length)
    print("Width:", width)
    print("Height:", height)
    print("Lateral Surface Area:", round(lateral_surface_area, 2))
    print("Total Surface Area:", round(total_surface_area, 2))

cuboidsurfacearea()