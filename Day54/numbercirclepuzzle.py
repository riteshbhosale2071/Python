def find():
    n = int(input("Enter a number: "))

    for i in range(1, n + 1):
        print(i, end=" ")

    for i in range(n - 1, 0, -1):
        print(i, end=" ")

find()