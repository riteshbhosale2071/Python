def find():
    t = (12, 21, 36, 44, 81)

    result = []

    for num in t:
        reverse = int(str(num)[::-1])

        if reverse != 0 and num % reverse == 0:
            result.append(num)

    print(tuple(result))

find()