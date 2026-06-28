def weeklyplanner():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]

    planner = {}

    for day in days:
        activity = input(f"Enter activity for {day}: ")
        planner[day] = activity

    print("\nWeekly Planner")
    print("-" * 30)

    for day in days:
        print(day, ":", planner[day])


weeklyplanner()