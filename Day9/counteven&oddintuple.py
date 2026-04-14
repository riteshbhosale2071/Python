T=(1,2,3,4,5,6,7,8,9)
print(T)
ce=0
co=0
for i in T:
    if i%2==0:
        ce+=1
    else:
        co+=1
print(f"Count of even in tuple is {ce}")
print(f"Count of odd in tuple is {co}")