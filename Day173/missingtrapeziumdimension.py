def missingtrapeziumdimension():
    print("Missing Trapezium Dimension Finder :")

    print("\nChoose the missing dimension:")
    print("1. First Parallel Side")
    print("2. Second Parallel Side")
    print("3. Height")

    choice = int(input("Enter your choice: "))
    area = float(input("Enter area of trapezium: "))

    if area <= 0:
        print("Area must be greater than zero.")
        return

    if choice == 1:
        second_side = float(input("Enter second parallel side: "))
        height = float(input("Enter height: "))

        if second_side <= 0 or height <= 0:
            print("Measurements must be greater than zero.")
            return

        first_side = (2 * area / height) - second_side

        if first_side <= 0:
            print("No valid first parallel side exists.")
        else:
            print("Missing First Parallel Side:", round(first_side, 2))

    elif choice == 2:
        first_side = float(input("Enter first parallel side: "))
        height = float(input("Enter height: "))

        if first_side <= 0 or height <= 0:
            print("Measurements must be greater than zero.")
            return

        second_side = (2 * area / height) - first_side

        if second_side <= 0:
            print("No valid second parallel side exists.")
        else:
            print("Missing Second Parallel Side:", round(second_side, 2))

    elif choice == 3:
        first_side = float(input("Enter first parallel side: "))
        second_side = float(input("Enter second parallel side: "))

        if first_side <= 0 or second_side <= 0:
            print("Measurements must be greater than zero.")
            return

        height = (2 * area) / (first_side + second_side)

        print("Missing Height:", round(height, 2))

    else:
        print("Invalid choice.")

missingtrapeziumdimension()