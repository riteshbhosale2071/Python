def find():
    t = ("aabb", "banana", "ccdd", "success")

    result = []

    for word in t:
        valid = True

        for ch in set(word):

            if word.count(ch) != 2:
                valid = False
                break

        if valid:
            result.append(word)

    print(tuple(result))

find()