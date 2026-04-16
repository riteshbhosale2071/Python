S={1,2,3,4,5,6,7,8,9}
print(S)
num=int(input("Enter value to check: "))
for i in S:
    if i==num:
        print(f"{num} found")
        break
else:
    print("Not found")