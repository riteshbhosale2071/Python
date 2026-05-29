def count():
    basket = input("Enter fruits separated by space: ").split()

    count = {}

    for fruit in basket:

        if fruit in count:
            count[fruit] += 1

        else:
            count[fruit] = 1

    print("Fruit Count =", count)

count()