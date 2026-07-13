def shaperotation():
    rows = int(input("Enter size: "))

    print("Original Shape:")
    for i in range(rows):
        print("* " * rows)

    print("\nRotated Shape:")
    for i in range(rows):
        for j in range(rows):
            print("*", end=" ")
        print()

shaperotation()