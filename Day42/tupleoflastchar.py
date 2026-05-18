def find():
    t = ("apple", "banana", "grape", "kiwi")

    result = []

    for word in t:
        result.append(word[-1])

    print(tuple(result))

find()