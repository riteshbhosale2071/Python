def piano():
    sessions = int(input("Enter number of practice sessions: "))

    total_keys = 0

    for i in range(sessions):
        keys = int(input(f"Enter keys pressed in session {i+1}: "))
        total_keys += keys

    print("Total Keys Pressed =", total_keys)

piano()