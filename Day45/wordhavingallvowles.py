def find():
    t = ("education", "sequoia", "apple", "automobile")

    result = []

    for word in t:
        vowels = "aeiou"

        found = True

        for v in vowels:

            if v not in word.lower():
                found = False
                break

        if found:
            result.append(word)

    print(tuple(result))

find()