def triangleperimeterandarea():
    print("Triangle Perimeter and Area Calculator")
    print("1. Calculate Perimeter")
    print("2. Calculate Area using Base and Height")
    print("3. Calculate Area using Heron's Formula")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
            perimeter = a + b + c
            print("Triangle Perimeter:", perimeter)
        else:
            print("Invalid triangle side lengths.")

    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        if base > 0 and height > 0:
            area = 0.5 * base * height
            print("Triangle Area:", area)
        else:
            print("Base and height must be positive.")

    elif choice == "3":
        a = float(input("Enter first side: "))
        b = float(input("Enter second side: "))
        c = float(input("Enter third side: "))

        if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
            print("Triangle Area:", round(area, 2))
        else:
            print("Invalid triangle side lengths.")

    else:
        print("Invalid choice.")

triangleperimeterandarea()