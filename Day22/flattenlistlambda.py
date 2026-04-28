from functools import reduce
L=[[1, 2], [3, 4], [5, 6]]
print(L)
flat = reduce(lambda a, b: a + b, L)
print(flat)