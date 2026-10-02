def boxmaterialcalculator():
    print("Box Material Calculator :")

    length = float(input("Enter box length: "))
    width = float(input("Enter box width: "))
    height = float(input("Enter box height: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("All dimensions must be greater than zero.")
        return

    material_area = 2 * (length * width + width * height + height * length)
    volume = length * width * height

    print("\nBox Length:", length)
    print("Box Width:", width)
    print("Box Height:", height)
    print("Material Required:", round(material_area, 2), "square units")
    print("Box Volume:", round(volume, 2), "cubic units")

boxmaterialcalculator()