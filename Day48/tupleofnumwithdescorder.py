def create():
    t = (937, 285, 176)

    result = []

    for num in t:
        digits = sorted(str(num), reverse=True)

        result.append(int("".join(digits)))

    print(tuple(result))

create()