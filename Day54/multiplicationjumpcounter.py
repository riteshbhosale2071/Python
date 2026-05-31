def counter():
    num = int(input("Enter number: "))
    limit = int(input("Enter limit: "))

    count = 0

    for i in range(num, limit + 1, num):

        print(i)

        count += 1

    print("\nTotal Jumps =", count)

counter()