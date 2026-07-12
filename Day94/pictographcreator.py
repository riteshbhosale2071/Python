def pictographcreator():
    item = input("Enter item name: ")
    count = int(input("Enter number of items: "))

    print("\nPictograph:")
    print(item + ":", end=" ")

    for i in range(count):
        print("★", end=" ")

    print()

pictographcreator()