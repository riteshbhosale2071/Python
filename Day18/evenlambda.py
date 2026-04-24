num=int(input("Enter any num: "))
res=lambda a:a%2==0
if res(num)==True:
    print(f"{num} is even")
else:
    print(f"{num} is not even")