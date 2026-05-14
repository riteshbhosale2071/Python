def split():
    t = ("cat", "elephant", "dog", "tiger", "ox")

    small = []
    large = []

    for word in t:
        if len(word) <= 3:
            small.append(word)
        else:
            large.append(word)

    print("Small Words:", tuple(small))
    print("Large Words:", tuple(large))

split()