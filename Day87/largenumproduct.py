def largenum():
    num1 = int(input("Enter the first large number: "))
    num2 = int(input("Enter the second large number: "))

    product = num1 * num2

    print("\nLarge Number Product Report")
    print("-" * 35)
    print("First Number  =", num1)
    print("Second Number =", num2)
    print("Product       =", product)

largenum()