def find():
    t = (421, 532, 908, 111)

    result = []

    for num in t:
        digits = sorted(str(num))
        result.append(int("".join(digits)))

    print(tuple(result))

find()