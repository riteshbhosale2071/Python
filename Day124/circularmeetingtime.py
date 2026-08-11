def circularmeetingtime():
    lap_times = list(map(int, input(
        "Enter lap times in seconds, separated by spaces: "
    ).split()))

    if not lap_times or any(time <= 0 for time in lap_times):
        print("Please enter positive lap times.")
        return

    def find_lcm(a, b):
        x, y = a, b

        while y != 0:
            x, y = y, x % y

        return abs(a * b) // x

    meeting_time = lap_times[0]

    for time in lap_times[1:]:
        meeting_time = find_lcm(meeting_time, time)

    print("They will meet at the starting point again after:",
          meeting_time, "seconds.")

circularmeetingtime()