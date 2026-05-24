def find():
    t = ("god", "dog", "live", "evil", "python")

    result = []

    for word in t:

        if word[::-1] in t and word != word[::-1]:
            result.append(word)

    print(tuple(result))

find()