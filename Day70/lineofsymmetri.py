def line():
    shape = input("Enter shape name: ").lower()

    if shape == "circle":
        print("Lines of Symmetry = Infinite")

    elif shape == "square":
        print("Lines of Symmetry = 4")

    elif shape == "rectangle":
        print("Lines of Symmetry = 2")

    elif shape == "equilateral triangle":
        print("Lines of Symmetry = 3")

    else:
        print("Shape information not available")

line()