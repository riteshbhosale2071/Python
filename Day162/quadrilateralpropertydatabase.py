def quadrilateralpropertydatabase():
    print("Quadrilateral Property Database :")
    print("1. Square")
    print("2. Rectangle")
    print("3. Parallelogram")
    print("4. Rhombus")
    print("5. Trapezium")
    print("6. Kite")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Shape: Square")
        print("Sides: All four sides are equal")
        print("Angles: All angles are 90 degrees")
        print("Opposite sides: Parallel")
        print("Diagonals: Equal and perpendicular")

    elif choice == 2:
        print("Shape: Rectangle")
        print("Sides: Opposite sides are equal")
        print("Angles: All angles are 90 degrees")
        print("Opposite sides: Parallel")
        print("Diagonals: Equal")

    elif choice == 3:
        print("Shape: Parallelogram")
        print("Sides: Opposite sides are equal")
        print("Angles: Opposite angles are equal")
        print("Opposite sides: Parallel")
        print("Diagonals: Bisect each other")

    elif choice == 4:
        print("Shape: Rhombus")
        print("Sides: All four sides are equal")
        print("Angles: Opposite angles are equal")
        print("Opposite sides: Parallel")
        print("Diagonals: Perpendicular and bisect each other")

    elif choice == 5:
        print("Shape: Trapezium")
        print("Sides: One pair of opposite sides is parallel")
        print("Angles: Adjacent angles on a leg are supplementary")
        print("Opposite sides: One pair is parallel")
        print("Diagonals: Depend on the type of trapezium")

    elif choice == 6:
        print("Shape: Kite")
        print("Sides: Two pairs of adjacent sides are equal")
        print("Angles: One pair of opposite angles is equal")
        print("Diagonals: Perpendicular")
        print("One diagonal bisects the other")

    else:
        print("Invalid choice.")

quadrilateralpropertydatabase()