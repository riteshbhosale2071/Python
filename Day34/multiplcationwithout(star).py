def mul():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = 0

    for i in range(b):
        result = result + a

    print("Multiplication =", result)

mul()