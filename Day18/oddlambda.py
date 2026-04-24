num=int(input("Enter any num: "))
res=lambda a:a%2==0
if res(num)==True:
    print(f"{num} is not odd")
else:
    print(f"{num} is odd")