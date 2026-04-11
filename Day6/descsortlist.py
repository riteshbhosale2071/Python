L=list()
num=int(input("Enter the amount of values of list: "))
for i in range(1,num+1):
    val=int(input(f"Enter value {i}: "))
    L.append(val)
print("List before sort: ",L)
L.sort(reverse=True)
print("List after sort: ",L)