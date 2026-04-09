num=int(input("Enter amount of value to add: "))
L=[]
for i in range(1,num+1):
    val=int(input(f"Enter value {i}:"))
    L.append(val)
print(L)
print(len(L))