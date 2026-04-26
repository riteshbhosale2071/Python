L=[1,2,3,4,5,6,7,8,9,10]
print("List:",L)
res=filter(lambda a:a%2==0, L)
print("Even from list is",list(res))