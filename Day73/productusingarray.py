def product():
    rows = int(input("Enter rows: "))
    
    columns = int(input("Enter columns: "))

    for i in range(rows):
        print("* " * columns)

    print("\nProduct =", rows * columns)

product()