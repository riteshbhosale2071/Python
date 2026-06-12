def lap():
    goal = int(input("Enter lap goal: "))
    
    completed = int(input("Enter laps completed: "))

    if completed >= goal:
        print("Lap Goal Achieved!")

    else:
        print("Laps Remaining =", goal - completed)

lap()