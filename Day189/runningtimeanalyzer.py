def runningtimeanalyzer():
    print("Running Time Analyzer :")

    n = int(input("Enter the number of running sessions: "))

    if n <= 0:
        print("Number of sessions must be greater than zero.")
        return

    running_times = []
    total_distance = 0
    total_time = 0

    for i in range(n):
        print("\nSession", i + 1)

        distance = float(input("Enter distance covered (km): "))
        time = float(input("Enter running time (minutes): "))

        if distance <= 0 or time <= 0:
            print("Distance and time must be greater than zero.")
            return

        running_times.append(time)
        total_distance += distance
        total_time += time

        speed = distance / (time / 60)
        pace = time / distance

        print("Average Speed:", round(speed, 2), "km/h")
        print("Running Pace:", round(pace, 2), "minutes/km")

    average_time = total_time / n
    average_distance = total_distance / n
    overall_speed = total_distance / (total_time / 60)
    overall_pace = total_time / total_distance

    fastest_time = min(running_times)
    slowest_time = max(running_times)

    print("\nRunning Performance Summary :")
    print("Total Sessions:", n)
    print("Total Distance:", round(total_distance, 2), "km")
    print("Total Running Time:", round(total_time, 2), "minutes")
    print("Average Distance per Session:", round(average_distance, 2), "km")
    print("Average Time per Session:", round(average_time, 2), "minutes")
    print("Overall Average Speed:", round(overall_speed, 2), "km/h")
    print("Overall Running Pace:", round(overall_pace, 2), "minutes/km")
    print("Shortest Session Time:", round(fastest_time, 2), "minutes")
    print("Longest Session Time:", round(slowest_time, 2), "minutes")

    print("\nPerformance Analysis :")

    if overall_pace < 5:
        print("Excellent pace! You are running faster than 5 minutes per kilometer.")
    elif overall_pace < 7:
        print("Good pace! Keep practicing to improve your speed.")
    else:
        print("Focus on building endurance and gradually improving your pace.")

    if fastest_time == slowest_time:
        print("Running times were consistent across all sessions.")
    else:
        print("Running times varied across sessions.")

runningtimeanalyzer()