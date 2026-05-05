n1 = int(input("Enter first num: "))
n2 = int(input("Enter second num: "))
n3 = int(input("Enter third num: "))
if n1 > n2 and n1 > n3:
    print(f"{n1} is greater")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is greater")
else:
    print(f"{n3} is greater")