def cubegrowth():
    print("Cube Growth Simulator :")

    start = int(input("Enter starting value: "))
    steps = int(input("Enter number of growth steps: "))

    if start < 0:
        print("Starting value cannot be negative.")
        return

    if steps < 1:
        print("Number of steps must be at least 1.")
        return

    print("\nCube Growth Simulation :")
    print(f"{'Step':<10}{'Value':<15}{'Cube':<15}")
    print("-" * 40)

    current = start

    for step in range(1, steps + 1):
        cube = current ** 3
        print(f"{step:<10}{current:<15}{cube:<15}")
        current += 1

    print("\nGrowth completed.")
    print("Final Value:", current - 1)
    print("Final Cube:", (current - 1) ** 3)

cubegrowth()