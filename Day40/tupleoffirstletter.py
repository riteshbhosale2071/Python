def find():
    t = ("Apple", "Banana", "Cherry", "Mango")

    letters = []

    for word in t:
        letters.append(word[0])

    print(tuple(letters))

find()