def cuboidsurfaceareaandvolumecalculator():
    print("Cuboid Surface Area and Volume Calculator")
    length = float(input("Enter cuboid length: "))
    breadth = float(input("Enter cuboid breadth: "))
    height = float(input("Enter cuboid height: "))

    if length <= 0 or breadth <= 0 or height <= 0:
        print("All dimensions must be positive.")
        return

    lateral_surface_area = 2 * height * (length + breadth)
    total_surface_area = 2 * (length * breadth + breadth * height + height * length)
    volume = length * breadth * height

    print("Lateral Surface Area =", round(lateral_surface_area, 2), "square units")
    print("Total Surface Area =", round(total_surface_area, 2), "square units")
    print("Volume =", round(volume, 2), "cubic units")

cuboidsurfaceareaandvolumecalculator()