def mul():
    t = (2, 3, 5)

    result = []

    for num in t:
        table = []

        for i in range(1, 11):
            table.append(num * i)

        result.append(tuple(table))

    print(tuple(result))

mul()