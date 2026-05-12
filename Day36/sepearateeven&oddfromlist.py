def find():
    L = [1, 2, 3, 4, 5, 6, 7, 8]
    odd = []
    even = []

    for i in L:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    print("List is =",L)
    print("Odd List =", odd)
    print("Even List =", even)

find()