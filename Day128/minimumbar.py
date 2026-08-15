def minimumbar():
    categories = input("Enter categories separated by spaces: ").split()
    values = list(map(int, input("Enter bar values separated by spaces: ").split()))

    if len(categories) != len(values):
        print("Number of categories and values must be equal.")
        return

    minimum = min(values)
    index = values.index(minimum)

    print("Minimum Bar:", categories[index])
    print("Minimum Value:", minimum)

minimumbar()