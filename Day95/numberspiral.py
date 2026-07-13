def numberspiral():
    rows = int(input("Enter number of rows: "))

    num = 1

    for i in range(rows):
        for j in range(rows):
            print(num, end="\t")
            num += 1
        print()

numberspiral()