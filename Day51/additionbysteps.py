def add():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    total = 0

    print("\nAddition Steps:")

    total += a
    print(total)

    total += b
    print(total)

    print("\nFinal Sum =", total)

add()