def shapearearanking():
    print("Shape Area Ranking :")

    number = int(input("Enter the number of shapes: "))

    if number <= 0:
        print("Number of shapes must be greater than zero.")
        return

    shapes = []

    for i in range(number):
        print("\nShape", i + 1)
        print("1. Rectangle")
        print("2. Square")
        print("3. Triangle")
        print("4. Circle")

        choice = int(input("Choose shape type: "))
        name = input("Enter shape name: ")

        if choice == 1:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            if length <= 0 or width <= 0:
                print("Invalid dimensions.")
                return

            area = length * width

        elif choice == 2:
            side = float(input("Enter side length: "))

            if side <= 0:
                print("Invalid dimension.")
                return

            area = side * side

        elif choice == 3:
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))

            if base <= 0 or height <= 0:
                print("Invalid dimensions.")
                return

            area = (base * height) / 2

        elif choice == 4:
            radius = float(input("Enter radius: "))

            if radius <= 0:
                print("Invalid dimension.")
                return

            area = 3.14159 * radius * radius

        else:
            print("Invalid shape choice.")
            return

        shapes.append([name, area])

    shapes.sort(key=lambda shape: shape[1], reverse=True)

    print("\nShape Area Ranking :")

    for i in range(number):
        print(i + 1, ".", shapes[i][0], "- Area:", round(shapes[i][1], 2))

    print("\nLargest Shape:", shapes[0][0])
    print("Largest Area:", round(shapes[0][1], 2))

    print("Smallest Shape:", shapes[-1][0])
    print("Smallest Area:", round(shapes[-1][1], 2))

shapearearanking()