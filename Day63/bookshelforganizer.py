def shelf():
    books = input("Enter book names separated by space: ").split()

    books.sort()

    print("Books on Shelf:")

    for book in books:
        print(book)

shelf()