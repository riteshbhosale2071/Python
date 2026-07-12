def fruitsales():
    fruit = input("Enter fruit name: ")
    sold = int(input("Enter number of fruits sold: "))

    print("\nFruit Sales Pictograph")
    print(fruit + ":", end=" ")

    for i in range(sold):
        print("#", end=" ")

    print()

fruitsales()