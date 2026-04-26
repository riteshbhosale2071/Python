L=[10,-2,-16,3,5,-65,64,34,2,-5]
print("List:",L)
res=filter(lambda a:a<0, L)
print("Negative num in list are",list(res))