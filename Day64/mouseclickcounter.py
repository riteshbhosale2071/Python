def click():
    total = 0

    n = int(input("How many clicks to record? "))

    for i in range(n):
        input("Press Enter for a click...")
        total += 1

    print("Total Clicks =", total)

click()