S=set()
size=int(input("Enter the size of set: "))
for i in range(1,size+1):
    num=int(input(f"Enter {i} value: "))
    S.add(num)
print(sorted(S))