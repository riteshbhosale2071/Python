def bookpurchase():
    books = int(input("Enter number of books: "))
    price = float(input("Enter price of one book: "))

    total = books * price

    print("Number of Books:", books)
    print("Price per Book:", price)
    print("Total Cost:", total)

bookpurchase()