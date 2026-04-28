from functools import reduce
L=[1,2,3,4,5,6,7,8,9]
res=reduce(lambda a, b: a + b, L)
print(res)