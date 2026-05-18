def find():
    t = (5, 6, 10, 25, 76)

    result = []

    for num in t:

        if str(num * num)[-1] == str(num)[-1]:
            result.append(num)

    print(tuple(result))

find()