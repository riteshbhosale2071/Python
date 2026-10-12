def cuboiddimensionsearch():
    print("Cuboid Dimension Search :")
    print("Find a missing dimension using volume and two known dimensions.")

    volume = float(input("Enter cuboid volume: "))
    print("1. Find Length")
    print("2. Find Width")
    print("3. Find Height")

    choice = input("Choose the dimension to find (1-3): ")

    if volume <= 0:
        print("Volume must be greater than zero.")
        return

    if choice == "1":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))

        if width <= 0 or height <= 0:
            print("Width and height must be greater than zero.")
            return

        length = volume / (width * height)
        print("Calculated Length:", round(length, 2))

    elif choice == "2":
        length = float(input("Enter length: "))
        height = float(input("Enter height: "))

        if length <= 0 or height <= 0:
            print("Length and height must be greater than zero.")
            return

        width = volume / (length * height)
        print("Calculated Width:", round(width, 2))

    elif choice == "3":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length <= 0 or width <= 0:
            print("Length and width must be greater than zero.")
            return

        height = volume / (length * width)
        print("Calculated Height:", round(height, 2))

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        return

    print("Verified Volume:", round(length * width * height, 2) if choice in ["1", "2", "3"] else volume)

cuboiddimensionsearch()