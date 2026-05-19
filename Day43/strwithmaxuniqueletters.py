def find():
    t = ("apple", "banana", "education", "strength")

    max_word = ""
    max_unique = 0

    for word in t:
        unique = len(set(word))

        if unique > max_unique:
            max_unique = unique
            max_word = word

    print("Word:", max_word)
    print("Unique Letters:", max_unique)

find()