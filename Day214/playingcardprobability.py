def playingcardprobability():
    print("Playing Card Probability Calculator")

    print("\nSelect an event:")
    print("1. Probability of drawing a red card")
    print("2. Probability of drawing a black card")
    print("3. Probability of drawing an Ace")
    print("4. Probability of drawing a King")
    print("5. Probability of drawing a Queen")
    print("6. Probability of drawing a face card")
    print("7. Probability of drawing a heart")
    print("8. Probability of drawing a spade")
    print("9. Probability of drawing a specific card")

    choice = int(input("\nEnter your choice: "))

    total_cards = 52
    favorable_cards = 0

    if choice == 1:
        favorable_cards = 26
        event = "Red Card"

    elif choice == 2:
        favorable_cards = 26
        event = "Black Card"

    elif choice == 3:
        favorable_cards = 4
        event = "Ace"

    elif choice == 4:
        favorable_cards = 4
        event = "King"

    elif choice == 5:
        favorable_cards = 4
        event = "Queen"

    elif choice == 6:
        favorable_cards = 12
        event = "Face Card"

    elif choice == 7:
        favorable_cards = 13
        event = "Heart"

    elif choice == 8:
        favorable_cards = 13
        event = "Spade"

    elif choice == 9:
        rank = input("Enter card rank (Ace, 2-10, Jack, Queen, King): ").strip().lower()
        suit = input("Enter suit (Hearts, Diamonds, Clubs, Spades): ").strip().lower()

        valid_ranks = ["ace", "2", "3", "4", "5", "6", "7",
                       "8", "9", "10", "jack", "queen", "king"]
        valid_suits = ["hearts", "diamonds", "clubs", "spades"]

        if rank not in valid_ranks or suit not in valid_suits:
            print("Invalid card rank or suit.")
            return

        favorable_cards = 1
        event = rank.title() + " of " + suit.title()

    else:
        print("Invalid choice.")
        return

    probability = favorable_cards / total_cards

    print("\nProbability Result :")
    print("Total Cards:", total_cards)
    print("Event:", event)
    print("Favorable Cards:", favorable_cards)
    print(f"Probability: {probability:.4f}")
    print(f"Percentage: {probability * 100:.2f}%")

playingcardprobability()