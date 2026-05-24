def create():
    t = (123456, 987654, 246810)

    result = []

    for num in t:
        s = str(num)

        new_num = s[::2]

        result.append(int(new_num))

    print(tuple(result))

create()