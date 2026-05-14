def compress():
    t = (1, 1, 1, 2, 2, 3, 3, 3, 3)

    compressed = []

    count = 1

    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            count += 1
        else:
            compressed.append((t[i], count))
            count = 1

    compressed.append((t[-1], count))

    print("Compressed Tuple:")
    print(tuple(compressed))

compress()