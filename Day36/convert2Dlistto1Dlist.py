def conv():
    L = [[1, 2], [3, 4], [5, 6]]
    new_list = []

    for i in L:
        
        for j in i:
            new_list.append(j)

    print("1D List =", new_list)

conv()