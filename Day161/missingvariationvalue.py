def missingvariationvalue():
    print("Missing Variation Value Finder :")
    print("1. Direct Variation: y = kx")
    print("2. Inverse Variation: xy = k")

    choice = int(input("Enter choice: "))

    if choice == 1:
        k = float(input("Enter variation constant k: "))
        value = float(input("Enter known value: "))
        find = input("Find x or y: ").lower()

        if find == "y":
            y = k * value
            print("Missing y =", y)

        elif find == "x":
            if k != 0:
                x = value / k
                print("Missing x =", x)
            else:
                print("k cannot be zero.")

        else:
            print("Invalid choice.")

    elif choice == 2:
        k = float(input("Enter variation constant k: "))
        value = float(input("Enter known value: "))
        find = input("Find x or y: ").lower()

        if value != 0:
            missing = k / value
            print("Missing", find, "=", missing)
        else:
            print("Known value cannot be zero.")

    else:
        print("Invalid choice.")

missingvariationvalue()