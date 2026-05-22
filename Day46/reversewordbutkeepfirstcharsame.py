def reverse():
    t = ("python", "tuple", "coding")

    result = []

    for word in t:
        new_word = word[0] + word[:0:-1]

        result.append(new_word)

    print(tuple(result))

reverse()