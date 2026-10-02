def cuboidmissingdimension():
    print("Cuboid Missing Dimension Solver :")

    print("\nChoose the missing dimension:")
    print("1. Length")
    print("2. Width")
    print("3. Height")

    choice = int(input("Enter your choice: "))
    surface_area = float(input("Enter total surface area: "))

    if surface_area <= 0:
        print("Surface area must be greater than zero.")
        return

    if choice == 1:
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if width <= 0 or height <= 0:
            print("Dimensions must be greater than zero.")
            return

        length = (surface_area / 2 - width * height) / (width + height)

        if length <= 0:
            print("No valid length can be found.")
        else:
            print("Missing Length:", round(length, 2))

    elif choice == 2:
        length = float(input("Enter length: "))
        height = float(input("Enter height: "))

        if length <= 0 or height <= 0:
            print("Dimensions must be greater than zero.")
            return

        width = (surface_area / 2 - length * height) / (length + height)

        if width <= 0:
            print("No valid width can be found.")
        else:
            print("Missing Width:", round(width, 2))

    elif choice == 3:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length <= 0 or width <= 0:
            print("Dimensions must be greater than zero.")
            return

        height = (surface_area / 2 - length * width) / (length + width)

        if height <= 0:
            print("No valid height can be found.")
        else:
            print("Missing Height:", round(height, 2))

    else:
        print("Invalid choice.")

cuboidmissingdimension()