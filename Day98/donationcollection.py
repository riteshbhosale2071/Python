def donation():
    n = int(input("Enter number of donations: "))
    
    total = 0
    for i in range(n):
        amount = float(input(f"Enter donation {i + 1}: "))
        total += amount

    average = total / n

    print("Total Donation =", total)
    print("Average Donation =", average)

donation()