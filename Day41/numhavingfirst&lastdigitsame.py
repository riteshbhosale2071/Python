def find():
    t = (121, 454, 789, 343, 908)

    result = []

    for num in t:
        s = str(num)

        if s[0] == s[-1]:
            result.append(num)

    print(tuple(result))

find()