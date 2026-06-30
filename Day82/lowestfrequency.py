def lowestfrequency():
    n = int(input("Enter number of elements: "))

    numbers = []

    for i in range(n):
        num = int(input(f"Enter element {i+1}: "))
        numbers.append(num)

    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    lowest = min(frequency, key=frequency.get)

    print("\nFrequency Table")
    print("-" * 25)

    for num, count in frequency.items():
        print(num, ":", count)

    print("\nElement with Lowest Frequency =", lowest)
    print("Frequency =", frequency[lowest])

lowestfrequency()