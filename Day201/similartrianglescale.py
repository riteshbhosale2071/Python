def similartrianglescale():
    print("Similar Triangle Scale Calculator")
    print("1. Find scale factor")
    print("2. Find missing side of second triangle")
    print("3. Find missing side of first triangle")

    choice = input("Enter your choice: ")

    if choice == "1":
        side1 = float(input("Enter side of first triangle: "))
        side2 = float(input("Enter corresponding side of second triangle: "))

        if side1 > 0 and side2 > 0:
            scale = side2 / side1
            print("Scale Factor:", round(scale, 2))
        else:
            print("Side lengths must be positive.")

    elif choice == "2":
        side1 = float(input("Enter side of first triangle: "))
        corresponding1 = float(input("Enter corresponding side of first triangle: "))
        corresponding2 = float(input("Enter corresponding side of second triangle: "))

        if side1 > 0 and corresponding1 > 0 and corresponding2 > 0:
            scale = corresponding2 / corresponding1
            missing_side = side1 * scale
            print("Missing side of second triangle:", round(missing_side, 2))
        else:
            print("Side lengths must be positive.")

    elif choice == "3":
        side2 = float(input("Enter side of second triangle: "))
        corresponding1 = float(input("Enter corresponding side of first triangle: "))
        corresponding2 = float(input("Enter corresponding side of second triangle: "))

        if side2 > 0 and corresponding1 > 0 and corresponding2 > 0:
            scale = corresponding1 / corresponding2
            missing_side = side2 * scale
            print("Missing side of first triangle:", round(missing_side, 2))
        else:
            print("Side lengths must be positive.")

    else:
        print("Invalid choice.")

similartrianglescale()