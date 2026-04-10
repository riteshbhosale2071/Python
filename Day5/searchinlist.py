L=[1,2,3,4,5,6,7,8,9]
num=int(input("Enter the value to search: "))
for i in L:
    if num==i:
        print(f"{num} found in list")
        break
else:
    print(f"{num} not in list")    