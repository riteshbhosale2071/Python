def polygonsidefinder():
    perimeter = float(input("Enter the perimeter of the polygon: "))
    sides = int(input("Enter the number of equal sides: "))

    if perimeter <= 0 or sides < 3:
        print("Enter a positive perimeter and at least 3 sides.")
        return

    side_length = perimeter / sides

    print("Number of Sides:", sides)
    print("Length of Each Side:", side_length)

polygonsidefinder()