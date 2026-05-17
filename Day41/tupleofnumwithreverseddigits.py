def find():
    t = (123, 456, 789)

    result = []

    for num in t:
        reverse = int(str(num)[::-1])
        result.append(reverse)

    print(tuple(result))

find()