def train():
    train = []

    while True:

        print("\n1. Add Coach")
        print("2. Remove Coach")
        print("3. Show Train")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            coach = int(input("Enter coach number: "))
            train.append(coach)

        elif choice == 2:

            if train:
                removed = train.pop(0)
                print("Removed Coach =", removed)
            else:
                print("Train is empty")

        elif choice == 3:

            print("Train =", train)

        elif choice == 4:
            break

        else:
            print("Invalid Choice")

train()