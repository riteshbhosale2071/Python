def elevatorfloor():
    current_floor = int(input("Enter the current floor: "))
    move = int(input("Enter floors to move (+ up, - down): "))

    new_floor = current_floor + move

    print("Current Floor:", current_floor)
    print("New Floor:", new_floor)

elevatorfloor()