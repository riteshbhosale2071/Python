def divarray():
    total_items = int(input("Enter the total number of items: "))
    columns = int(input("Enter the number of columns: "))

    if columns <= 0:
        print("Number of columns must be greater than 0.")
        return

    rows = total_items // columns
    remainder = total_items % columns

    print("\nDivision Using Arrays")
    print("-" * 35)

    for i in range(rows):
        for j in range(columns):
            print("*", end=" ")
        print()

    if remainder > 0:
        print("\nRemaining Items:", end=" ")
        for i in range(remainder):
            print("*", end=" ")

    print("\n")
    print("Rows =", rows)
    print("Columns =", columns)
    print("Quotient =", rows)
    print("Remainder =", remainder)

divarray()