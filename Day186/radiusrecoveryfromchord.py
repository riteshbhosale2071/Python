def radiusrecoveryfromchord():
    print("Radius Recovery from Chord :")
    print("1. Calculate radius using chord length and distance from center")
    print("2. Calculate radius using chord length and sagitta")

    choice = input("Choose a method (1-2): ")

    if choice == "1":
        chord = float(input("Enter full chord length: "))
        distance = float(input("Enter perpendicular distance from center to chord: "))

        if chord <= 0 or distance < 0:
            print("Chord length must be positive and distance cannot be negative.")
            return

        half_chord = chord / 2
        radius = ((half_chord ** 2) + (distance ** 2)) ** 0.5

    elif choice == "2":
        chord = float(input("Enter full chord length: "))
        sagitta = float(input("Enter sagitta (height from chord to arc): "))

        if chord <= 0 or sagitta <= 0:
            print("Chord length and sagitta must be greater than zero.")
            return

        half_chord = chord / 2
        radius = ((half_chord ** 2) + (sagitta ** 2)) / (2 * sagitta)

    else:
        print("Invalid choice. Select 1 or 2.")
        return

    diameter = 2 * radius
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * radius ** 2

    print("\nRadius Recovery Results :")
    print("Chord Length:", round(chord, 4))
    print("Recovered Radius:", round(radius, 4))
    print("Circle Diameter:", round(diameter, 4))
    print("Circle Circumference:", round(circumference, 4))
    print("Circle Area:", round(area, 4))

    print("Radius recovery completed successfully.")

radiusrecoveryfromchord()