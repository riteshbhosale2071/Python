def cubemeasurementcalculator():
    print("Cube Measurement Calculator")
    print("1. Calculate Volume")
    print("2. Calculate Total Surface Area")
    print("3. Calculate Lateral Surface Area")
    print("4. Calculate Face Diagonal")
    print("5. Calculate Space Diagonal")
    print("6. Calculate Perimeter of One Face")

    choice = input("Enter your choice (1-6): ")

    try:
        side = float(input("Enter the side length of the cube: "))

        if side <= 0:
            print("Side length must be greater than zero.")
            return

        if choice == "1":
            result = side ** 3
            print("Volume:", round(result, 2), "cubic units")

        elif choice == "2":
            result = 6 * side ** 2
            print("Total Surface Area:", round(result, 2), "square units")

        elif choice == "3":
            result = 4 * side ** 2
            print("Lateral Surface Area:", round(result, 2), "square units")

        elif choice == "4":
            result = side * (2 ** 0.5)
            print("Face Diagonal:", round(result, 2), "units")

        elif choice == "5":
            result = side * (3 ** 0.5)
            print("Space Diagonal:", round(result, 2), "units")

        elif choice == "6":
            result = 4 * side
            print("Perimeter of One Face:", round(result, 2), "units")

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

    except ValueError:
        print("Please enter a valid numeric value.")

cubemeasurementcalculator()