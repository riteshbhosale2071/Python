def create():
    t = ("python", "tuple", "advanced", "coding")

    result = []

    for word in t:
        result.append(word[1:-1])

    print(tuple(result))

create()