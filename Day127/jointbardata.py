def jointbardata():
    categories = input("Enter categories separated by spaces: ").split()
    data1 = list(map(int, input("Enter first data set: ").split()))
    data2 = list(map(int, input("Enter second data set: ").split()))

    if len(categories) != len(data1) or len(categories) != len(data2):
        print("Number of categories and data values must be equal.")
        return

    print("\nJoint Bar Data:")
    for i in range(len(categories)):
        print(f"{categories[i]}: {data1[i]} | {data2[i]}")

    print("\nComparison:")
    for i in range(len(categories)):
        if data1[i] > data2[i]:
            print(f"{categories[i]}: First data set is higher.")
        elif data1[i] < data2[i]:
            print(f"{categories[i]}: Second data set is higher.")
        else:
            print(f"{categories[i]}: Both are equal.")

jointbardata()