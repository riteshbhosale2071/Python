L1 = [1, 2, 3]
L2 = [4, 5, 6]
result = list(map(lambda x: x[0] + x[1], zip(L1, L2)))
print(result)