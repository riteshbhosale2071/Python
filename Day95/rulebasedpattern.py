def rulebased():
    start = int(input("Enter starting number: "))
    rule = int(input("Enter number to add each time: "))
    terms = int(input("Enter number of terms: "))

    print("Pattern:")

    for i in range(terms):
        print(start, end=" ")
        start = start + rule

rulebased()