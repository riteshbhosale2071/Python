L=[1,2,3,4,5,6,7,8,9]
print("List:",L)
res=list(filter(lambda a: a > 1 and all(a % i != 0 for i in range(2, a)), L))
print("Prime num in list are",list(res))