def mul():
    rows = int(input("Enter number of rows: "))
    
    cols = int(input("Enter number of columns: "))

    for i in range(rows):
        print("* " * cols)

mul()