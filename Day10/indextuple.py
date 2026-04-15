T=(1,2,3,4,5,6,7,8,9)
print(T)
num=int(input("Enter the value to get index: "))
for i in T:
    if i==num:
        print(f"Value found at index ",T.index(num))
        break
else:
    print("Value not in tuple")