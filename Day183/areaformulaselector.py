def areaformulaselector():
    print("Area Formula Selector :")
    print("1. Square")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Circle")
    print("5. Parallelogram")
    print("6. Trapezium")
    print("7. Rhombus")

    choice = input("Select a shape (1-7): ")

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid selection. Please choose a number from 1 to 7.")
        return

    if choice == "1":
        side = float(input("Enter side length: "))

        if side <= 0:
            print("Side length must be greater than zero.")
            return

        area = side * side
        formula = "side × side"
        shape = "Square"

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        if length <= 0 or width <= 0:
            print("Length and width must be greater than zero.")
            return

        area = length * width
        formula = "length × width"
        shape = "Rectangle"

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))

        if base <= 0 or height <= 0:
            print("Base and height must be greater than zero.")
            return

        area = 0.5 * base * height
        formula = "1/2 × base × height"
        shape = "Triangle"

    elif choice == "4":
        radius = float(input("Enter radius: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        area = 3.14159 * radius * radius
        formula = "π × radius²"
        shape = "Circle"

    elif choice == "5":
        base = float(input("Enter base: "))
        height = float(input("Enter perpendicular height: "))

        if base <= 0 or height <= 0:
            print("Base and height must be greater than zero.")
            return

        area = base * height
        formula = "base × height"
        shape = "Parallelogram"

    elif choice == "6":
        a = float(input("Enter first parallel side: "))
        b = float(input("Enter second parallel side: "))
        height = float(input("Enter perpendicular height: "))

        if a <= 0 or b <= 0 or height <= 0:
            print("All dimensions must be greater than zero.")
            return

        area = 0.5 * (a + b) * height
        formula = "1/2 × (a + b) × height"
        shape = "Trapezium"

    else:
        d1 = float(input("Enter first diagonal: "))
        d2 = float(input("Enter second diagonal: "))

        if d1 <= 0 or d2 <= 0:
            print("Both diagonals must be greater than zero.")
            return

        area = 0.5 * d1 * d2
        formula = "1/2 × diagonal 1 × diagonal 2"
        shape = "Rhombus"

    print("\nArea Calculation Result :")
    print("Shape:", shape)
    print("Formula:", formula)
    print("Area:", round(area, 2), "square units")

areaformulaselector()