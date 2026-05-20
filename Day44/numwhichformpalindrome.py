def find():
    t = (121, 343, 456, 787, 890)

    result = []

    for num in t:

        if str(num) == str(num)[::-1]:
            result.append(num)

    print(tuple(result))

find()