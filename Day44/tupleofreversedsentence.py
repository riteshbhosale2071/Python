def find():
    t = (
        "Python is fun",
        "Tuple programs",
        "Practice coding"
    )

    result = []

    for sentence in t:
        result.append(sentence[::-1])

    print(tuple(result))

find()