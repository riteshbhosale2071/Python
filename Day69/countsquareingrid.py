def grid():
    n = int(input("Enter grid size (N): "))

    total = n * (n + 1) * (2 * n + 1) // 6

    print("Total Squares =", total)

grid()