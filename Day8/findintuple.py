T=(1,2,3,4,5,6,7,8,9)
print(T)
num=int(input("Enter value to search: "))
for i in T:
    if i == num:
        print(f"{num} found in tuple")
        break
else:
    print(f"{num} not found")