def cutoutareacalc():
    print("Cut-Out Area Calculator :")

    print("\nChoose the main shape:")
    print("1. Rectangle")
    print("2. Circle")
    print("3. Triangle")

    main_choice = int(input("Enter choice: "))

    if main_choice == 1:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length <= 0 or width <= 0:
            print("Invalid dimensions.")
            return

        main_area = length * width

    elif main_choice == 2:
        radius = float(input("Enter radius: "))

        if radius <= 0:
            print("Invalid radius.")
            return

        main_area = 3.14159 * radius * radius

    elif main_choice == 3:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        if base <= 0 or height <= 0:
            print("Invalid dimensions.")
            return

        main_area = 0.5 * base * height

    else:
        print("Invalid main shape.")
        return

    number_of_cutouts = int(input("\nEnter number of cut-outs: "))

    if number_of_cutouts < 0:
        print("Number of cut-outs cannot be negative.")
        return

    total_cutout_area = 0

    for i in range(number_of_cutouts):
        print("\nCut-Out", i + 1)
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")

        cutout_choice = int(input("Enter cut-out shape: "))

        if cutout_choice == 1:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length <= 0 or width <= 0:
                print("Invalid dimensions.")
                return

            cutout_area = length * width

        elif cutout_choice == 2:
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Invalid radius.")
                return

            cutout_area = 3.14159 * radius * radius

        elif cutout_choice == 3:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            cutout_area = 0.5 * base * height

        else:
            print("Invalid cut-out shape.")
            return

        total_cutout_area += cutout_area

    if total_cutout_area > main_area:
        print("\nError: Total cut-out area cannot be greater than the main shape area.")
        return

    remaining_area = main_area - total_cutout_area

    print("\nMain Shape Area:", round(main_area, 2))
    print("Total Cut-Out Area:", round(total_cutout_area, 2))
    print("Remaining Area:", round(remaining_area, 2))

cutoutareacalc()