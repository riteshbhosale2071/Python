def find():
    t = ("committee", "apple", "coffee", "bookkeeper")

    result = []

    for word in t:
        doubles = 0

        for i in range(len(word) - 1):

            if word[i] == word[i + 1]:
                doubles += 1

        if doubles > 1:
            result.append(word)

    print(tuple(result))

find()