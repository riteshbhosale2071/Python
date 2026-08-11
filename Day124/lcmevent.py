def lcmevent():
    intervals = list(map(int, input(
        "Enter event intervals in minutes, separated by spaces: "
    ).split()))

    if not intervals or any(interval <= 0 for interval in intervals):
        print("Please enter positive intervals.")
        return

    def find_lcm(a, b):
        x, y = a, b

        while y != 0:
            x, y = y, x % y

        return abs(a * b) // x

    common_time = intervals[0]

    for interval in intervals[1:]:
        common_time = find_lcm(common_time, interval)

    print("Events will occur simultaneously again after:",
          common_time, "minutes.")

lcmevent()