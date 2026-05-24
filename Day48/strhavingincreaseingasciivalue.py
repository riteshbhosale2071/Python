def find():
    t = ("abc", "ace", "cat", "xyz")

    result = []

    for word in t:
        valid = True

        for i in range(len(word) - 1):

            if ord(word[i]) >= ord(word[i + 1]):
                valid = False
                break

        if valid:
            result.append(word)

    print(tuple(result))

find()