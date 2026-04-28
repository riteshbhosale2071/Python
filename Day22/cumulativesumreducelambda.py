from functools import reduce
L=[1, 2, 3, 4, 5]
res=reduce(lambda x, y: x + y, L)
print("Total sum:", res)