def inverseproportionvalidator():
    n = int(input("Enter the number of data pairs: "))

    if n < 2:
        print("Enter at least 2 data pairs.")
        return

    data = []

    for i in range(n):
        print(f"\nData Pair {i + 1}:")
        x = float(input("Enter X: "))
        y = float(input("Enter Y: "))

        if x == 0 or y == 0:
            print("X and Y cannot be zero.")
            return

        product = x * y
        data.append((x, y, product))

    constant_product = data[0][2]
    is_inverse = True

    for x, y, product in data:
        if product != constant_product:
            is_inverse = False
            break

    print("\nInverse Proportion Validation")
    print("Constant Product (X × Y):", constant_product)

    if is_inverse:
        print("The data follows Inverse Proportion.")
    else:
        print("The data does not follow Inverse Proportion.")

inverseproportionvalidator()