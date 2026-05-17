def create():
    t = ("python", "programming", "tuple")

    result = []

    for word in t:
        result.append(word[::2])

    print(tuple(result))

create()