L1 = [1, 2, 3, 4]
L2 = [3, 4, 5, 6]
result = list(filter(lambda x: x in L2, L1))
print(result)