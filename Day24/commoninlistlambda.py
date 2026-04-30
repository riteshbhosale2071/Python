L1 = [1, 2, 3, 4]
L2 = [2, 3, 5]
L3 = [2, 3, 6]
result=list(set(L1) & set(L2) & set(L3))
print(result)