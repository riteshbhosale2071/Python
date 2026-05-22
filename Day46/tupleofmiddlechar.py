def find():
    t = ("apple", "banana", "grape", "kiwi")

    result = []

    for word in t:
        mid = len(word) // 2

        result.append(word[mid])

    print(tuple(result))

find()