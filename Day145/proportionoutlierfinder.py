def proportionoutlierfinder():
    n = int(input("Enter the number of data pairs: "))

    if n < 3:
        print("Enter at least 3 data pairs.")
        return

    data = []

    for i in range(n):
        print(f"\nData Pair {i + 1}:")
        x = float(input("Enter X: "))
        y = float(input("Enter Y: "))

        if x == 0:
            print("X cannot be zero.")
            return

        ratio = y / x
        data.append((x, y, ratio))

    average_ratio = sum(item[2] for item in data) / n

    outlier = max(
        data,
        key=lambda item: abs(item[2] - average_ratio)
    )

    print("\nProportion Outlier Analysis :")
    print("Average Ratio:", average_ratio)

    print("\nRatios:")
    for i, (x, y, ratio) in enumerate(data, start=1):
        print(f"Pair {i}: {ratio}")

    print("\nPotential Outlier:")
    print("X =", outlier[0])
    print("Y =", outlier[1])
    print("Ratio =", outlier[2])

proportionoutlierfinder()