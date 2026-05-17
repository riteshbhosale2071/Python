def find():
    t = ("apple", "banana", "kiwi", "grapes")

    lengths = []

    for word in t:
        lengths.append(len(word))

    print(tuple(lengths))

find()