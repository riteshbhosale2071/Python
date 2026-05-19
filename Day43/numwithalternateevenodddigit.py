def find():
    t = (1234, 2468, 1357, 1212)

    result = []

    for num in t:
        s = str(num)

        valid = True

        for i in range(len(s) - 1):

            if int(s[i]) % 2 == int(s[i + 1]) % 2:
                valid = False
                break

        if valid:
            result.append(num)

    print(tuple(result))

find()