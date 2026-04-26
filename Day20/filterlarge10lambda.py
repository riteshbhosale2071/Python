L=[10,2,16,3,5,65,64,34,2,5]
print("List:",L)
res=filter(lambda a:a>10, L)
print("Greater than 10 in list is",list(res))