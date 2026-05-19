def find():
    t = ("python programming", "tuple methods", "advanced code")

    result = []

    for word in t:
        result.append(word.replace(" ", "-"))

    print(tuple(result))

find()