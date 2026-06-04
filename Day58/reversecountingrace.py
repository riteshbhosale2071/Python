def count():
    start = int(input("Enter starting number: "))

    print("Reverse Counting Race:\n")

    for i in range(start, 0, -1):
        print(i)

    print("\nFinish Line!")

count()