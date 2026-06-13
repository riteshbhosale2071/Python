def dance():
    goal = int(input("Enter dance step goal: "))
    completed = int(input("Enter steps completed: "))

    if completed >= goal:
        print("Dance Goal Achieved!")

    else:
        print("Steps Remaining =", goal - completed)

dance()