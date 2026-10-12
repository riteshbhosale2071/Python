def boxcapacitycalculator():
    print("Box Capacity Calculator :")

    length = float(input("Enter box length: "))
    width = float(input("Enter box width: "))
    height = float(input("Enter box height: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("All dimensions must be greater than zero.")
        return

    volume = length * width * height

    print("\nBox Capacity Results :")
    print("Length:", length)
    print("Width:", width)
    print("Height:", height)
    print("Box Volume:", round(volume, 2), "cubic units")

    print("\nCapacity Conversions:")
    print("Cubic Centimeters:", round(volume, 2), "cm³")
    print("Liters:", round(volume / 1000, 3), "L")
    print("Cubic Meters:", round(volume / 1000000, 6), "m³")

    items = float(input("\nEnter the volume of one item in cubic units: "))

    if items <= 0:
        print("Item volume must be greater than zero.")
        return

    capacity = int(volume // items)
    remaining = volume - (capacity * items)

    print("\nMaximum Whole Items That Fit:", capacity)
    print("Unused Volume:", round(remaining, 2), "cubic units")

boxcapacitycalculator()