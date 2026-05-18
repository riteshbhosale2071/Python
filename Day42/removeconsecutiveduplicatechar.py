def find():
    t = ("baalloon", "aappple", "book")

    result = []

    for word in t:
        new_word = word[0]

        for ch in word[1:]:

            if ch != new_word[-1]:
                new_word += ch

        result.append(new_word)

    print(tuple(result))

find()