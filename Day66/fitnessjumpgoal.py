def goal():
    goal = int(input("Enter jump goal: "))
    
    completed = int(input("Enter jumps completed: "))

    if completed >= goal:
        print("Goal Achieved!")

    else:
        print("Jumps Remaining =", goal - completed)

goal()