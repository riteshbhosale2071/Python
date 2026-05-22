def find():
    t = ("banana", "idea", "tiger", "code")

    result = []

    for word in t:
        valid = True

        for i in range(len(word) - 1):

            first = word[i] in "aeiou"
            second = word[i + 1] in "aeiou"

            if first == second:
                valid = False
                break

        if valid:
            result.append(word)

    print(tuple(result))

find()