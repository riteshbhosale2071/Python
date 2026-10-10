def arearatiocalculator():
    print("Area Ratio Calculator :")

    print("1. Rectangle and Rectangle")
    print("2. Square and Square")
    print("3. Circle and Circle")
    print("4. Triangle and Triangle")
    print("5. Trapezium and Trapezium")

    choice = int(input("Select shape type: "))

    if choice == 1:
        length1 = float(input("Enter first rectangle length: "))
        width1 = float(input("Enter first rectangle width: "))
        length2 = float(input("Enter second rectangle length: "))
        width2 = float(input("Enter second rectangle width: "))

        area1 = length1 * width1
        area2 = length2 * width2

    elif choice == 2:
        side1 = float(input("Enter first square side: "))
        side2 = float(input("Enter second square side: "))

        area1 = side1 ** 2
        area2 = side2 ** 2

    elif choice == 3:
        radius1 = float(input("Enter first circle radius: "))
        radius2 = float(input("Enter second circle radius: "))

        area1 = 3.14159 * radius1 ** 2
        area2 = 3.14159 * radius2 ** 2

    elif choice == 4:
        base1 = float(input("Enter first triangle base: "))
        height1 = float(input("Enter first triangle height: "))
        base2 = float(input("Enter second triangle base: "))
        height2 = float(input("Enter second triangle height: "))

        area1 = 0.5 * base1 * height1
        area2 = 0.5 * base2 * height2

    elif choice == 5:
        a1 = float(input("Enter first trapezium's first parallel side: "))
        b1 = float(input("Enter first trapezium's second parallel side: "))
        h1 = float(input("Enter first trapezium's height: "))
        a2 = float(input("Enter second trapezium's first parallel side: "))
        b2 = float(input("Enter second trapezium's second parallel side: "))
        h2 = float(input("Enter second trapezium's height: "))

        area1 = 0.5 * (a1 + b1) * h1
        area2 = 0.5 * (a2 + b2) * h2

    else:
        print("Invalid choice.")
        return

    if area1 <= 0 or area2 <= 0:
        print("All dimensions must be greater than zero.")
        return

    ratio = area1 / area2

    print("\nArea Ratio Result :")
    print("First Shape Area:", round(area1, 2))
    print("Second Shape Area:", round(area2, 2))
    print("Area Ratio:", round(ratio, 2), ": 1")

    if area1 > area2:
        print("The first shape has the larger area.")
    elif area2 > area1:
        print("The second shape has the larger area.")
    else:
        print("Both shapes have equal areas.")

arearatiocalculator()