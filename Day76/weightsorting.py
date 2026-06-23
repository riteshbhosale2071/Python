def sorting():
    n = int(input("Enter number of weights: "))

    weights = []

    for i in range(n):
        weight = float(input(f"Enter weight {i+1}: "))
        weights.append(weight)

    weights.sort()

    print("Weights in Ascending Order:")
    print(weights)

sorting()