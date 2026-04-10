L=[1,2,3,4,5,6,7,8,9]
print(L)
count=0
check=int(input("Enter value to check :"))
for i in L:
    if(check==i):
        print(f"{check} found at index {count}")
    count+=1