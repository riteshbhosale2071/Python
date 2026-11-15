def samplespace():
    print("Sample Space Generator")
    print("1. Coin Toss")
    print("2. Two Coin Tosses")
    print("3. Dice Roll")
    print("4. Two Dice Rolls")
    print("5. Custom Number Range")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sample_space = ["Heads", "Tails"]

    elif choice == 2:
        sample_space = [
            ("Heads", "Heads"),
            ("Heads", "Tails"),
            ("Tails", "Heads"),
            ("Tails", "Tails")
        ]

    elif choice == 3:
        sample_space = list(range(1, 7))

    elif choice == 4:
        sample_space = [
            (i, j)
            for i in range(1, 7)
            for j in range(1, 7)
        ]

    elif choice == 5:
        start = int(input("Enter starting number: "))
        end = int(input("Enter ending number: "))

        if start > end:
            print("Invalid range.")
            return

        sample_space = list(range(start, end + 1))

    else:
        print("Invalid choice.")
        return

    print("\nSample Space:")
    for outcome in sample_space:
        print(outcome)

    print("\nTotal Number of Possible Outcomes:", len(sample_space))

samplespace()