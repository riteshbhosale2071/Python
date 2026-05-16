def find():
    t = (12, 45, 21, 54, 78, 87)

    result = []

    for num in t:
        reverse = int(str(num)[::-1])

        if reverse in t:
            result.append(num)

    print("Numbers whose reverse exists:")
    print(tuple(result))

find()