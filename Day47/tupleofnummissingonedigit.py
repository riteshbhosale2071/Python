def tuplefun():
    t = (1234, 5678, 9012)

    result = []

    for num in t:
        s = str(num)
        new_num = int(s[:-1])

        result.append(new_num)

    print(tuple(result))

tuplefun()