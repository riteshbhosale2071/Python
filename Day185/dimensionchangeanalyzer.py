def dimensionchangeanalyzer():
    print("Dimension Change Analyzer :")

    length = float(input("Enter original length: "))
    width = float(input("Enter original width: "))
    height = float(input("Enter original height: "))

    length_factor = float(input("Enter length scaling factor: "))
    width_factor = float(input("Enter width scaling factor: "))
    height_factor = float(input("Enter height scaling factor: "))

    if length <= 0 or width <= 0 or height <= 0:
        print("Original dimensions must be greater than zero.")
        return

    if length_factor <= 0 or width_factor <= 0 or height_factor <= 0:
        print("Scaling factors must be greater than zero.")
        return

    original_volume = length * width * height
    original_surface_area = 2 * (
        length * width + width * height + length * height
    )

    new_length = length * length_factor
    new_width = width * width_factor
    new_height = height * height_factor

    new_volume = new_length * new_width * new_height
    new_surface_area = 2 * (
        new_length * new_width
        + new_width * new_height
        + new_height * new_length
    )

    volume_change = new_volume - original_volume
    surface_change = new_surface_area - original_surface_area

    volume_percentage = (volume_change / original_volume) * 100
    surface_percentage = (surface_change / original_surface_area) * 100

    print("\nOriginal Dimensions :")
    print("Length:", length)
    print("Width:", width)
    print("Height:", height)
    print("Original Volume:", round(original_volume, 2))
    print("Original Surface Area:", round(original_surface_area, 2))

    print("\nNew Dimensions :")
    print("Length:", round(new_length, 2))
    print("Width:", round(new_width, 2))
    print("Height:", round(new_height, 2))
    print("New Volume:", round(new_volume, 2))
    print("New Surface Area:", round(new_surface_area, 2))

    print("\nChange Analysis :")
    print("Volume Difference:", round(volume_change, 2))
    print("Volume Percentage Change:", round(volume_percentage, 2), "%")
    print("Surface Area Difference:", round(surface_change, 2))
    print("Surface Area Percentage Change:", round(surface_percentage, 2), "%")

    if volume_change > 0:
        print("Volume has increased.")
    elif volume_change < 0:
        print("Volume has decreased.")
    else:
        print("Volume remains unchanged.")

    if surface_change > 0:
        print("Surface area has increased.")
    elif surface_change < 0:
        print("Surface area has decreased.")
    else:
        print("Surface area remains unchanged.")

dimensionchangeanalyzer()