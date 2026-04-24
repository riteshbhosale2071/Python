num1=int(input("Enter first num: "))
num2=int(input("Enter second num: "))
res=lambda a,b:a>b
if res(num1,num2)==True:
    print(f"{num2} is small than {num1}")
else:
    print(f"{num1} is small than {num2}")