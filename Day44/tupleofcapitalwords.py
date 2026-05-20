def find():
    t = ("python", "tuple", "advanced", "coding")

    result = []

    for word in t:
        result.append(word.capitalize())

    print(tuple(result))

find()