def find():
    t = ("PyThOn", "TuPlE", "CoDiNg")

    result = []

    for word in t:
        result.append(word.swapcase())

    print(tuple(result))

find()