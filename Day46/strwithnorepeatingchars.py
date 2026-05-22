def find():
    t = ("apple", "banana", "kite", "moon")

    result = []

    for word in t:
        valid = True

        for i in range(len(word) - 1):

            if word[i] == word[i + 1]:
                valid = False
                break

        if valid:
            result.append(word)

    print(tuple(result))

find()