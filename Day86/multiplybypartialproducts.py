def partialproducts():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    ones = num2 % 10
    tens = (num2 // 10) % 10
    hundreds = num2 // 100

    print("\nPartial Products")
    print("-" * 35)

    total = 0

    if ones > 0:
        partial = num1 * ones
        print(f"{num1} × {ones} = {partial}")
        total += partial

    if tens > 0:
        partial = num1 * tens * 10
        print(f"{num1} × {tens} × 10 = {partial}")
        total += partial

    if hundreds > 0:
        partial = num1 * hundreds * 100
        print(f"{num1} × {hundreds} × 100 = {partial}")
        total += partial

    print("-" * 35)
    print("Final Product =", total)

partialproducts()