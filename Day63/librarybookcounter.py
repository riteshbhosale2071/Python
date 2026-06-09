def library():
    total_books = int(input("Enter total books: "))
    
    issued_books = int(input("Enter issued books: "))

    available_books = total_books - issued_books

    print("Available Books =", available_books)

library()