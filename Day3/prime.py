num=int(input("Enter any number: "))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")
else:
    print("Enter a num greater than 1")