def watertank():
    length = float(input("Enter length (m): "))
    width = float(input("Enter width (m): "))
    height = float(input("Enter height (m): "))

    capacity = length * width * height

    print("Water Tank Capacity:", capacity, "cubic meters")

watertank()