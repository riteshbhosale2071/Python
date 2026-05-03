from functools import reduce
print(reduce(lambda a,b:a+b, map(lambda x:x*x, filter(lambda x:x%2==0, [1,2,3,4,5]))))