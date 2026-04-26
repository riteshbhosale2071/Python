L=[10, 15, 30, 7, 9, 45]
print("List:",L)
res=list(filter(lambda a:a%3==0 and a%5==0,L))
print("Num divisible by 3 and 5 are",res)