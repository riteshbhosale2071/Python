def find():
    cards = [1, 2, 3, 4, 1, 2, 3, 4]

    num = int(input("Enter a card number (1-4): "))

    count = cards.count(num)

    if count == 2:
        print("Pair Matched!")

    else:
        print("No Pair Found")

find()