def square():
    n = int(input("Enter size: "))

    for i in range(n):
        for j in range(n):
            print(j + 1, end=" ")
        print()

square()