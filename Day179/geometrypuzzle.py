def geometrypuzzle():
    print("Geometry Puzzle Generator :")
    print("1. Triangle Puzzle")
    print("2. Rectangle Puzzle")
    print("3. Circle Puzzle")
    print("4. Square Puzzle")

    choice = int(input("Select puzzle type: "))

    if choice == 1:
        side1 = float(input("Enter first side: "))
        side2 = float(input("Enter second side: "))

        if side1 <= 0 or side2 <= 0:
            print("Enter valid side lengths.")
            return

        print("\nPuzzle:")
        print("A triangle has two sides of", side1, "and", side2)
        print("and a perimeter of 30 units.")
        print("Find the third side.")

        third_side = 30 - side1 - side2

        if third_side > 0 and side1 + side2 > third_side:
            print("Answer:", round(third_side, 2))
        else:
            print("The given values cannot form a valid triangle.")

    elif choice == 2:
        area = float(input("Enter rectangle area: "))
        length = float(input("Enter rectangle length: "))

        if area <= 0 or length <= 0:
            print("Enter valid values.")
            return

        print("\nPuzzle:")
        print("A rectangle has an area of", area, "square units")
        print("and a length of", length, "units.")
        print("Find the width and perimeter.")

        width = area / length
        perimeter = 2 * (length + width)

        print("Width:", round(width, 2))
        print("Perimeter:", round(perimeter, 2))

    elif choice == 3:
        radius = float(input("Enter circle radius: "))
        angle = float(input("Enter sector angle: "))

        if radius <= 0 or angle <= 0 or angle > 360:
            print("Enter valid values.")
            return

        pi = 3.14159

        print("\nPuzzle:")
        print("A circular sector has radius", radius, "units")
        print("and central angle", angle, "degrees.")
        print("Find its area and arc length.")

        sector_area = (angle / 360) * pi * radius ** 2
        arc_length = (angle / 360) * 2 * pi * radius

        print("Sector Area:", round(sector_area, 2))
        print("Arc Length:", round(arc_length, 2))

    elif choice == 4:
        perimeter = float(input("Enter square perimeter: "))

        if perimeter <= 0:
            print("Perimeter must be greater than zero.")
            return

        print("\nPuzzle:")
        print("A square has a perimeter of", perimeter, "units.")
        print("Find its side length, area, and diagonal.")

        side = perimeter / 4
        area = side ** 2
        diagonal = side * (2 ** 0.5)

        print("Side Length:", round(side, 2))
        print("Area:", round(area, 2))
        print("Diagonal:", round(diagonal, 2))

    else:
        print("Invalid puzzle type.")

geometrypuzzle()