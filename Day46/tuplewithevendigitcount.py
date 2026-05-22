def count():
    t = (12, 4567, 890, 123456, 78)

    result = []

    for num in t:

        if len(str(num)) % 2 == 0:
            result.append(num)

    print(tuple(result))

count()