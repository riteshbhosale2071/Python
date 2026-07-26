def raydirection():
    start = int(input("Enter starting point: "))
    end = int(input("Enter ending point: "))

    if end > start:
        print("Ray is in the Positive Direction")
    elif end < start:
        print("Ray is in the Negative Direction")
    else:
        print("Invalid Ray")

raydirection()