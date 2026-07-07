def treecounter():
    rows = int(input("Enter number of rows: "))
    trees_per_row = int(input("Enter trees in each row: "))

    total_trees = rows * trees_per_row

    print("Total Trees:", total_trees)

treecounter()