def netpuzzle():
    shape = input("Enter 3D shape: ").lower()

    if shape == "cube":
        print("Puzzle: Arrange 6 squares to make a cube net.")
    elif shape == "cuboid":
        print("Puzzle: Arrange 6 rectangles to make a cuboid net.")
    elif shape == "cylinder":
        print("Puzzle: Arrange 2 circles and 1 rectangle.")
    elif shape == "cone":
        print("Puzzle: Arrange 1 circle and 1 sector.")
    else:
        print("Shape not found.")

netpuzzle()