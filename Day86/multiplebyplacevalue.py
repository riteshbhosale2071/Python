def multiply():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print("\nPlace Value Multiplication")
    print("-" * 35)

    total = 0
    place = 1
    temp = num2

    while temp > 0:
        digit = temp % 10
        partial_product = num1 * digit * place

        print(f"{num1} × {digit} × {place} = {partial_product}")

        total += partial_product
        place *= 10
        temp //= 10

    print("-" * 35)
    print("Final Product =", total)

multiply()