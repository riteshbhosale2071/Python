def swap():
    D = {'a':1, 'b':2, 'c':3}

    max_key = max(D, key=D.get)
    min_key = min(D, key=D.get)

    D[max_key], D[min_key] = D[min_key], D[max_key]

    print(D)

swap()