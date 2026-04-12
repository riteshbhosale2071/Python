L=[1,2,3,9]
print(L)
num=L[3]
for i in range(1,num+1):
    if i not in L:
        print(i,end=" ")
print("values are not in list")