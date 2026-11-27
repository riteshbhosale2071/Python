def cubemeasurementcalculator():
    print("Cube Measurement Calculator")
    print("1. Calculate Volume")
    print("2. Calculate Total Surface Area")
    print("3. Calculate Lateral Surface Area")
    print("4. Calculate Face Diagonal")
    print("5. Calculate Space Diagonal")
    print("6. Calculate Edge Length")

    choice = input("Enter your choice (1-6): ")

    if choice in ("1", "2", "3", "4", "5"):
        side = float(input("Enter cube side length: "))

        if side <= 0:
            print("Side length must be positive.")
            return

        if choice == "1":
            result = side ** 3
            label = "Volume"
        elif choice == "2":
            result = 6 * side ** 2
            label = "Total Surface Area"
        elif choice == "3":
            result = 4 * side ** 2
            label = "Lateral Surface Area"
        elif choice == "4":
            result = side * 2 ** 0.5
            label = "Face Diagonal"
        else:
            result = side * 3 ** 0.5
            label = "Space Diagonal"

        print(label, "=", round(result, 2))

    elif choice == "6":
        volume = float(input("Enter cube volume: "))

        if volume <= 0:
            print("Volume must be positive.")
            return

        side = volume ** (1 / 3)
        print("Edge Length =", round(side, 2))

    else:
        print("Invalid choice.")

cubemeasurementcalculator()