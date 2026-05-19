def find():
    t = ("apple", "banana", "grape")

    result = []

    for word in t:
        chars = ""

        for ch in word:

            if word.count(ch) == 1:
                chars += ch

        result.append(chars)

    print(tuple(result))

find()