def formulainversion():
    print("Formula Inversion :")
    print("1. Speed = Distance / Time")
    print("2. Area of Rectangle = Length × Width")
    print("3. Simple Interest = (P × R × T) / 100")
    print("4. Triangle Area = (Base × Height) / 2")
    print("5. Circle Area = π × Radius²")

    choice = int(input("Select a formula: "))

    if choice == 1:
        print("\n1. Find Distance")
        print("2. Find Speed")
        print("3. Find Time")

        option = int(input("Select what to find: "))

        if option == 1:
            speed = float(input("Enter speed: "))
            time = float(input("Enter time: "))
            if speed >= 0 and time >= 0:
                print("Distance:", round(speed * time, 2))
            else:
                print("Enter valid values.")

        elif option == 2:
            distance = float(input("Enter distance: "))
            time = float(input("Enter time: "))
            if distance >= 0 and time > 0:
                print("Speed:", round(distance / time, 2))
            else:
                print("Enter valid values.")

        elif option == 3:
            distance = float(input("Enter distance: "))
            speed = float(input("Enter speed: "))
            if distance >= 0 and speed > 0:
                print("Time:", round(distance / speed, 2))
            else:
                print("Enter valid values.")

        else:
            print("Invalid option.")

    elif choice == 2:
        print("\n1. Find Length")
        print("2. Find Width")

        option = int(input("Select what to find: "))

        if option == 1:
            area = float(input("Enter area: "))
            width = float(input("Enter width: "))
            if area > 0 and width > 0:
                print("Length:", round(area / width, 2))
            else:
                print("Enter valid values.")

        elif option == 2:
            area = float(input("Enter area: "))
            length = float(input("Enter length: "))
            if area > 0 and length > 0:
                print("Width:", round(area / length, 2))
            else:
                print("Enter valid values.")

        else:
            print("Invalid option.")

    elif choice == 3:
        print("\n1. Find Principal")
        print("2. Find Rate")
        print("3. Find Time")

        option = int(input("Select what to find: "))

        if option == 1:
            interest = float(input("Enter simple interest: "))
            rate = float(input("Enter rate: "))
            time = float(input("Enter time: "))
            if interest >= 0 and rate > 0 and time > 0:
                principal = (interest * 100) / (rate * time)
                print("Principal:", round(principal, 2))
            else:
                print("Enter valid values.")

        elif option == 2:
            interest = float(input("Enter simple interest: "))
            principal = float(input("Enter principal: "))
            time = float(input("Enter time: "))
            if interest >= 0 and principal > 0 and time > 0:
                rate = (interest * 100) / (principal * time)
                print("Rate:", round(rate, 2), "%")
            else:
                print("Enter valid values.")

        elif option == 3:
            interest = float(input("Enter simple interest: "))
            principal = float(input("Enter principal: "))
            rate = float(input("Enter rate: "))
            if interest >= 0 and principal > 0 and rate > 0:
                time = (interest * 100) / (principal * rate)
                print("Time:", round(time, 2))
            else:
                print("Enter valid values.")

        else:
            print("Invalid option.")

    elif choice == 4:
        print("\n1. Find Base")
        print("2. Find Height")

        option = int(input("Select what to find: "))

        if option == 1:
            area = float(input("Enter area: "))
            height = float(input("Enter height: "))
            if area > 0 and height > 0:
                base = (2 * area) / height
                print("Base:", round(base, 2))
            else:
                print("Enter valid values.")

        elif option == 2:
            area = float(input("Enter area: "))
            base = float(input("Enter base: "))
            if area > 0 and base > 0:
                height = (2 * area) / base
                print("Height:", round(height, 2))
            else:
                print("Enter valid values.")

        else:
            print("Invalid option.")

    elif choice == 5:
        radius = float(input("Enter radius: "))
        area = float(input("Enter circle area: "))

        if area > 0:
            radius_from_area = (area / 3.14159) ** 0.5
            print("Radius from given area:", round(radius_from_area, 2))

        elif radius > 0:
            circle_area = 3.14159 * radius ** 2
            print("Area:", round(circle_area, 2))

        else:
            print("Enter valid values.")

    else:
        print("Invalid formula selection.")

formulainversion()