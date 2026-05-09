def age():
    n1 = int(input("Enter first age:"))
    n2 = int(input("Enter second age:"))
    n3 = int(input("Enter third age:"))

    if n1 > n2 and n1 > n2:
        print(f"{n1} is oldest in age")
    elif n2 > n1 and n2 > n3:
        print(f"{n2} is oldest in age")
    else:
        print(f"{n3} is oldest in age")

age()