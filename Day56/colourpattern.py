def colour():
    colors = ["Red", "Green", "Blue"]

    rows = int(input("Enter number of rows: "))

    for i in range(rows):

        print(colors[i % len(colors)])

colour()