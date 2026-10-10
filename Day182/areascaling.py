def areascaling():
    print("Area Scaling :")

    print("1. Rectangle")
    print("2. Square")
    print("3. Triangle")
    print("4. Circle")

    choice = int(input("Select a shape: "))
    scale_factor = float(input("Enter linear scaling factor: "))

    if scale_factor <= 0:
        print("Scaling factor must be greater than zero.")
        return

    if choice == 1:
        length = float(input("Enter rectangle length: "))
        width = float(input("Enter rectangle width: "))

        if length <= 0 or width <= 0:
            print("Dimensions must be greater than zero.")
            return

        original_area = length * width

    elif choice == 2:
        side = float(input("Enter square side: "))

        if side <= 0:
            print("Side must be greater than zero.")
            return

        original_area = side ** 2

    elif choice == 3:
        base = float(input("Enter triangle base: "))
        height = float(input("Enter triangle height: "))

        if base <= 0 or height <= 0:
            print("Dimensions must be greater than zero.")
            return

        original_area = 0.5 * base * height

    elif choice == 4:
        radius = float(input("Enter circle radius: "))

        if radius <= 0:
            print("Radius must be greater than zero.")
            return

        original_area = 3.14159 * radius ** 2

    else:
        print("Invalid choice.")
        return

    new_area = original_area * scale_factor ** 2
    area_change = new_area - original_area

    print("\nScaling Results :")
    print("Original Area:", round(original_area, 2))
    print("Linear Scaling Factor:", scale_factor)
    print("Area Scaling Factor:", round(scale_factor ** 2, 2))
    print("New Area:", round(new_area, 2))
    print("Change in Area:", round(area_change, 2))

    if area_change > 0:
        print("The area increased.")
    elif area_change < 0:
        print("The area decreased.")
    else:
        print("The area remained unchanged.")

areascaling()