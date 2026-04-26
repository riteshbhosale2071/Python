L=[1,2,3,4,5,6,7,8,9,10]
print("List:",L)
res=filter(lambda a:a%2==1, L)
print("Odd from list is",list(res))