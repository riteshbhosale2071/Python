def openboxsurfaceareacalculator():
    print("Open Box Surface Area Calculator :")

    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("All dimensions must be greater than zero.")
        return

    base_area = length * width
    side_area_1 = length * height
    side_area_2 = width * height

    open_surface_area = base_area + (2 * side_area_1) + (2 * side_area_2)

    print("\nBase Area:", round(base_area, 2))
    print("Side Area 1:", round(side_area_1, 2))
    print("Side Area 2:", round(side_area_2, 2))
    print("Open Box Surface Area:", round(open_surface_area, 2))

openboxsurfaceareacalculator()