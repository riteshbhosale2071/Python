def trianglescalefactor():
    print("Triangle Scale Factor Calculator")
    print("1. Find Scale Factor")
    print("2. Find New Side Length")
    print("3. Find Original Side Length")
    print("4. Find Area Scale Factor")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        original = float(input("Enter original side length: "))
        new = float(input("Enter corresponding new side length: "))

        if original <= 0 or new <= 0:
            print("Side lengths must be positive.")
            return

        scale = new / original
        print("Scale Factor =", round(scale, 4))

    elif choice == "2":
        original = float(input("Enter original side length: "))
        scale = float(input("Enter scale factor: "))

        if original <= 0 or scale <= 0:
            print("Values must be positive.")
            return

        print("New Side Length =", round(original * scale, 2))

    elif choice == "3":
        new = float(input("Enter new side length: "))
        scale = float(input("Enter scale factor: "))

        if new <= 0 or scale <= 0:
            print("Values must be positive.")
            return

        print("Original Side Length =", round(new / scale, 2))

    elif choice == "4":
        scale = float(input("Enter scale factor: "))

        if scale <= 0:
            print("Scale factor must be positive.")
            return

        print("Area Scale Factor =", round(scale ** 2, 4))

    else:
        print("Invalid choice.")

trianglescalefactor()