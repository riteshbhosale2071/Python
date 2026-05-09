def swap():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    print("Before swap:")
    print("N1 =",n1)
    print("N2 =",n2)
    temp = 0
    temp = n1
    n1 = n2
    n2 = temp
    print("After swap:")
    print("N1 =",n1)
    print("N2 =",n2)

swap()