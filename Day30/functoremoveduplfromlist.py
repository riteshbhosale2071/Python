def duplicatelist(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    print(y)

duplicatelist([1,1,2,3,3,4])