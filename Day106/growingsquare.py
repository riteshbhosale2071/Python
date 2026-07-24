def growingsquare():
    rows = int(input("Enter size: "))

    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

growingsquare()