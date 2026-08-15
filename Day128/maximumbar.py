def maximumbar():
    categories = input("Enter categories separated by spaces: ").split()
    values = list(map(int, input("Enter bar values separated by spaces: ").split()))

    if len(categories) != len(values):
        print("Number of categories and values must be equal.")
        return

    maximum = max(values)
    index = values.index(maximum)

    print("Maximum Bar:", categories[index])
    print("Maximum Value:", maximum)

maximumbar()