L1 = [1, 2, 3, 4, 5]
L2 = [3, 4, 6]
result = list(filter(lambda x: x not in L2, L1))
print(result)