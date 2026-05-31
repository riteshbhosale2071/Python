def traffic():
    while True:

        print("\n1. Red")
        print("2. Yellow")
        print("3. Green")
        print("4. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print("STOP")

        elif choice == 2:
            print("WAIT")

        elif choice == 3:
            print("GO")

        elif choice == 4:
            print("Simulator Closed")
            break

        else:
            print("Invalid Choice")

traffic()