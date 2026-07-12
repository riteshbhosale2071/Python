def tabletopictograph():
    item = input("Enter item name: ")
    count = int(input("Enter quantity: "))

    print("\nPictograph:")
    print(item + ":", end=" ")

    for i in range(count):
        print("*", end=" ")

    print()

tabletopictograph()