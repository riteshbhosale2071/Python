def replace():
    t = ("apple", "orange", "umbrella")

    result = []

    for word in t:
        new_word = ""

        for ch in word:
            if ch.lower() in "aeiou":
                new_word += "*"
            else:
                new_word += ch

        result.append(new_word)

    print(tuple(result))

replace()