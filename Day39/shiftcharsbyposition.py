def shift():
    t = ("abc", "xyz", "hello")

    result = []

    for word in t:
        new_word = ""

        for ch in word:
            new_word += chr(ord(ch) + 1)

        result.append(new_word)

    print(tuple(result))

shift()