def find():
    t = ("apple", "lamp", "kite", "banana")

    result = []

    for word in t:

        if len(word) == len(set(word)):
            result.append(word)

    print("Words with Unique Characters:")
    print(tuple(result))

find()