def find():
    t = ("beautiful", "apple", "queue", "sky")

    result = []

    for word in t:

        for i in range(len(word) - 1):

            if word[i] in "aeiou" and word[i + 1] in "aeiou":
                result.append(word)
                break

    print(tuple(result))

find()