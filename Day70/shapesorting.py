def shape():
    shapes = input("Enter shape names separated by space: ").split()

    shapes.sort()

    print("Sorted Shapes:")

    for shape in shapes:
        print(shape)

shape()