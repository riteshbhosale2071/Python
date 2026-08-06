def geometrytool():
    print("Geometry Tool Identifier")
    print("1. Compass")
    print("2. Ruler")
    print("3. Protractor")
    print("4. Set Square")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        print("Compass: Used to draw circles and arcs.")
    elif choice == 2:
        print("Ruler: Used to draw and measure straight lines.")
    elif choice == 3:
        print("Protractor: Used to measure and draw angles.")
    elif choice == 4:
        print("Set Square: Used to draw perpendicular and parallel lines.")
    else:
        print("Invalid Choice!")

geometrytool()