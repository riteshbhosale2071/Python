num1=int(input("Enter starting no: "))
num2=int(input("Enter ending no: "))
for i in range(num1,num2+1):
    if(i%2==0):
        print(f"{i} ", end='')