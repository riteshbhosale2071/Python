def newspaper():
    n = int(input("Enter number of newspapers: "))

    total_pages = 0

    for i in range(n):
        pages = int(input("Enter pages in newspaper: "))
        total_pages += pages

    print("Total Pages =", total_pages)

newspaper()