def count():
    rows = int(input("Enter number of triangle rows: "))

    total = rows * (rows + 1) // 2

    print("Total Triangles =", total)

count()