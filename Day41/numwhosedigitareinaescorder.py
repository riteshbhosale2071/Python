def sort():
    t = (123, 321, 456, 654, 789)

    result = []

    for num in t:
        s = str(num)

        if list(s) == sorted(s):
            result.append(num)

    print(tuple(result))

sort()