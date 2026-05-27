def count():
    items = int(input("Enter total items: "))

    bundle = items // 10
    singles = items % 10

    print("Bundles =", bundle)
    print("Singles =", singles)

count()