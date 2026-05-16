def convert():
    t = ("python programming", "tuple methods", "advanced code")

    result = []

    for word in t:
        result.append(word.title())

    print(tuple(result))

convert()