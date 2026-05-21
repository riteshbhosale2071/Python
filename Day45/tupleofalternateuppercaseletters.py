def find():
    t = ("python", "tuple", "advanced")

    result = []

    for word in t:
        new_word = ""

        for i in range(len(word)):

            if i % 2 == 0:
                new_word += word[i].upper()
            else:
                new_word += word[i]

        result.append(new_word)

    print(tuple(result))

find()