def find():
    position = 0

    while True:

        print("\nCurrent Position =", position)

        print("1. Jump Forward")
        print("2. Jump Backward")
        print("3. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:

            step = int(input("Enter forward jump: "))
            position += step

        elif choice == 2:

            step = int(input("Enter backward jump: "))
            position -= step

        elif choice == 3:

            print("Game Over")
            break

        else:
            print("Invalid Choice")

find()