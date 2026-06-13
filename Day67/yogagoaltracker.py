def yoga():
    goal = int(input("Enter yoga pose goal: "))
    completed = int(input("Enter poses completed: "))

    if completed >= goal:
        print("Yoga Goal Achieved!")

    else:
        print("Poses Remaining =", goal - completed)

yoga()