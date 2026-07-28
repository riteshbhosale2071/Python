def integernumline():
    start = int(input("Enter the starting integer: "))
    end = int(input("Enter the ending integer: "))

    print("Number Line:")
    for i in range(start, end + 1):
        print(i, end=" ")

integernumline()