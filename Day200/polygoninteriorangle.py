def polygoninteriorangle():
    print("Polygon Interior Angle Calculator")
    print("1. Calculate sum of interior angles")
    print("2. Calculate each interior angle of a regular polygon")

    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2":
        sides = int(input("Enter the number of sides: "))

        if sides < 3:
            print("A polygon must have at least 3 sides.")
        else:
            total = (sides - 2) * 180

            if choice == "1":
                print("Sum of interior angles:", total, "degrees")
            else:
                angle = total / sides
                print("Each interior angle:", angle, "degrees")
    else:
        print("Invalid choice.")

polygoninteriorangle()