def sorting():
    shapes = ["circle", "square", "triangle", "circle", "square"]

    sorted_shapes = {}

    for shape in shapes:

        if shape in sorted_shapes:
            sorted_shapes[shape] += 1

        else:
            sorted_shapes[shape] = 1

    print(sorted_shapes)

sorting()