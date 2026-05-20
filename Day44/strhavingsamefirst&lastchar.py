def find():
    t = ("level", "apple", "radar", "python", "madam")

    result = []

    for word in t:

        if word[0] == word[-1]:
            result.append(word)

    print(tuple(result))

find()