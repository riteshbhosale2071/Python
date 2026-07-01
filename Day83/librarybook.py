def library():
    n = int(input("Enter number of books: "))

    books = {}
    total_books = 0

    for i in range(n):
        category = input(f"Enter category of book {i+1}: ").capitalize()

        if category in books:
            books[category] += 1
        else:
            books[category] = 1

        total_books += 1

    print("\nLibrary Book Statistics")
    print("-" * 35)

    for category, count in books.items():
        print(category, ":", count)

    highest = max(books, key=books.get)
    lowest = min(books, key=books.get)

    print("\nTotal Books =", total_books)
    print("Most Books Category =", highest)
    print("Least Books Category =", lowest)

library()