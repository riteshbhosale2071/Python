def integerpair():
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

    positive = 0
    negative = 0
    zero = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]

            if product > 0:
                positive += 1
            elif product < 0:
                negative += 1
            else:
                zero += 1

    print("Positive Product Pairs:", positive)
    print("Negative Product Pairs:", negative)
    print("Zero Product Pairs:", zero)

integerpair()