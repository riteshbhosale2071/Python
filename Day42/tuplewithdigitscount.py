def find():
    t = (1234, 56, 78901, 8)

    result = []

    for num in t:
        result.append(len(str(num)))

    print(tuple(result))

find()