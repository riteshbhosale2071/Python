def minimumpartitioncalculator():
    print("Minimum Partition Calculator :")

    sides = int(input("Enter number of polygon sides: "))

    if sides < 3:
        print("A polygon must have at least 3 sides.")
        return

    print("\n1. Minimum triangles to partition a polygon")
    print("2. Minimum diagonals required")
    print("3. Minimum cuts to divide a polygon into triangles")

    choice = int(input("Select an option: "))

    if choice == 1:
        triangles = sides - 2
        print("Minimum Triangles Required:", triangles)

    elif choice == 2:
        diagonals = sides - 3
        print("Minimum Diagonals from One Vertex:", diagonals)

    elif choice == 3:
        cuts = sides - 3
        print("Minimum Internal Cuts Required:", cuts)

    else:
        print("Invalid choice.")

minimumpartitioncalculator()