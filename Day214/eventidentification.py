def eventidentification():
    print("Event Identification Program")
    print("1. Coin Toss")
    print("2. Dice Roll")
    print("3. Two Coin Tosses")
    print("4. Two Dice Rolls")

    choice = int(input("Select an experiment: "))

    if choice == 1:
        sample_space = ["Heads", "Tails"]
        event = input("Enter event (Heads/Tails): ").capitalize()

    elif choice == 2:
        sample_space = list(range(1, 7))
        event = int(input("Enter dice outcome (1-6): "))

    elif choice == 3:
        sample_space = [
            ("Heads", "Heads"),
            ("Heads", "Tails"),
            ("Tails", "Heads"),
            ("Tails", "Tails")
        ]
        event = input("Enter event (HH, HT, TH, TT): ").upper()

        event_map = {
            "HH": ("Heads", "Heads"),
            "HT": ("Heads", "Tails"),
            "TH": ("Tails", "Heads"),
            "TT": ("Tails", "Tails")
        }

        if event not in event_map:
            print("Invalid event.")
            return

        event = event_map[event]

    elif choice == 4:
        sample_space = [
            (i, j)
            for i in range(1, 7)
            for j in range(1, 7)
        ]
        first = int(input("Enter first dice outcome (1-6): "))
        second = int(input("Enter second dice outcome (1-6): "))

        if first not in range(1, 7) or second not in range(1, 7):
            print("Invalid dice outcome.")
            return

        event = (first, second)

    else:
        print("Invalid choice.")
        return

    if event in sample_space:
        print("\nEvent Identified:", event)
        print("Event is possible in the sample space.")
        print("Probability of Event:", 1 / len(sample_space))
    else:
        print("\nEvent is not possible in the sample space.")

eventidentification()