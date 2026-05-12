def count():
    string = input("Enter a string: ")

    words = string.split()

    count = len(words)

    print("Number of words =", count)

count()