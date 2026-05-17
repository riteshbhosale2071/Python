def reverse():
    t = ("apple", "banana", "grape", "mango", "kiwi")

    result = []

    for i in range(len(t)):

        if i % 2 == 0:
            result.append(t[i][::-1])
        else:
            result.append(t[i])

    print(tuple(result))

reverse()