def cuboidmeasurementcalculator():
    print("Cuboid Measurement Calculator")
    print("1. Calculate Volume")
    print("2. Calculate Total Surface Area")
    print("3. Calculate Lateral Surface Area")
    print("4. Calculate Space Diagonal")
    print("5. Calculate Sum of All Edges")
    print("6. Calculate Base Area")

    choice = input("Enter your choice (1-6): ")

    try:
        length = float(input("Enter length of cuboid: "))
        breadth = float(input("Enter breadth of cuboid: "))
        height = float(input("Enter height of cuboid: "))

        if length <= 0 or breadth <= 0 or height <= 0:
            print("All dimensions must be greater than zero.")
            return

        if choice == "1":
            result = length * breadth * height
            print("Volume:", round(result, 2), "cubic units")

        elif choice == "2":
            result = 2 * (length * breadth + breadth * height + height * length)
            print("Total Surface Area:", round(result, 2), "square units")

        elif choice == "3":
            result = 2 * height * (length + breadth)
            print("Lateral Surface Area:", round(result, 2), "square units")

        elif choice == "4":
            result = (length ** 2 + breadth ** 2 + height ** 2) ** 0.5
            print("Space Diagonal:", round(result, 2), "units")

        elif choice == "5":
            result = 4 * (length + breadth + height)
            print("Sum of All Edges:", round(result, 2), "units")

        elif choice == "6":
            result = length * breadth
            print("Base Area:", round(result, 2), "square units")

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    except ValueError:
        print("Please enter valid numeric dimensions.")

cuboidmeasurementcalculator()