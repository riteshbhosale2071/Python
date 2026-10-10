def equalareashapechecker():
    print("Equal-Area Shape Checker :")

    print("1. Rectangle and Triangle")
    print("2. Square and Rectangle")
    print("3. Circle and Square")
    print("4. Trapezium and Rectangle")

    choice = int(input("Select two shapes to compare: "))

    if choice == 1:
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))

        area1 = length * width
        area2 = 0.5 * base * height
        name1 = "Rectangle"
        name2 = "Triangle"

    elif choice == 2:
        side = float(input("Enter square side: "))
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        area1 = side * side
        area2 = length * width
        name1 = "Square"
        name2 = "Rectangle"

    elif choice == 3:
        radius = float(input("Enter circle radius: "))
        side = float(input("Enter square side: "))

        area1 = 3.14159 * radius * radius
        area2 = side * side
        name1 = "Circle"
        name2 = "Square"

    elif choice == 4:
        a = float(input("Enter first parallel side of trapezium: "))
        b = float(input("Enter second parallel side of trapezium: "))
        height = float(input("Enter trapezium height: "))
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        area1 = 0.5 * (a + b) * height
        area2 = length * width
        name1 = "Trapezium"
        name2 = "Rectangle"

    else:
        print("Invalid choice.")
        return

    if area1 <= 0 or area2 <= 0:
        print("All dimensions must be greater than zero.")
        return

    difference = abs(area1 - area2)

    print("\nArea Comparison :")
    print(name1, "Area:", round(area1, 2))
    print(name2, "Area:", round(area2, 2))
    print("Area Difference:", round(difference, 2))

    if difference < 0.01:
        print("Result: Both shapes have approximately equal areas.")
    elif area1 > area2:
        print("Result:", name1, "has the larger area.")
    else:
        print("Result:", name2, "has the larger area.")

equalareashapechecker()