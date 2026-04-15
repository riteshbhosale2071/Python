T=(1,2,3,4,5,6,7,8,9)
print(T)
num=int(input("Enter the value: "))
for i in T:
    if i==num:
        print(f"Value found in tuple ")
        break
else:
    print("Value not in tuple")