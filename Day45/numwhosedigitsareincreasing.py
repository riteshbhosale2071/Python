def find():
    t = (123, 135, 122, 567, 455)

    result = []

    for num in t:
        s = str(num)

        increasing = True

        for i in range(len(s) - 1):

            if s[i] >= s[i + 1]:
                increasing = False
                break

        if increasing:
            result.append(num)

    print(tuple(result))

find()