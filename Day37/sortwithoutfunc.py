def sorting():
    L = [5, 2, 8, 1, 9, 3]

    for i in range(len(L)):

        for j in range(0, len(L)-i-1):

            if L[j] > L[j+1]:

                L[j], L[j+1] = L[j+1], L[j]

    print("Sorted List =", L)

sorting()