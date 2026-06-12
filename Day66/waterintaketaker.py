def water():
    goal = int(input("Enter daily water goal (glasses): "))
    
    consumed = int(input("Enter glasses consumed: "))

    if consumed >= goal:
        print("Daily Goal Achieved")

    else:
        print("More Glasses Needed =", goal - consumed)

water()