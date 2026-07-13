def squarenumber():
    rows = int(input("Enter number of rows: "))

    for i in range(1, rows + 1):
        for j in range(rows):
            print(i * i, end=" ")
        print()

squarenumber()