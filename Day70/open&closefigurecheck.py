def figure():
    shape = input("Enter shape name: ").lower()

    closed_shapes = ["circle", "square", "rectangle", "triangle", "pentagon"]

    if shape in closed_shapes:
        print("Closed Figure")

    else:
        print("Open Figure")

figure()