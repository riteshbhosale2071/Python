def tuplefunc():
    t = ("apple", "banana", "grape")

    result = []

    for word in t:
        shifted = word[1:] + word[0]
        result.append(shifted)

    print(tuple(result))

tuplefunc()