def missingtriangleside():
    print("Missing Triangle Side Calculator")
    print("1. Find hypotenuse")
    print("2. Find first perpendicular side")
    print("3. Find second perpendicular side")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))

        if a > 0 and b > 0:
            c = (a ** 2 + b ** 2) ** 0.5
            print("Missing hypotenuse:", round(c, 2))
        else:
            print("Side lengths must be positive.")

    elif choice == "2":
        b = float(input("Enter second side: "))
        c = float(input("Enter hypotenuse: "))

        if b > 0 and c > b:
            a = (c ** 2 - b ** 2) ** 0.5
            print("Missing first side:", round(a, 2))
        else:
            print("Invalid side lengths.")

    elif choice == "3":
        a = float(input("Enter first side: "))
        c = float(input("Enter hypotenuse: "))

        if a > 0 and c > a:
            b = (c ** 2 - a ** 2) ** 0.5
            print("Missing second side:", round(b, 2))
        else:
            print("Invalid side lengths.")

    else:
        print("Invalid choice.")

missingtriangleside()