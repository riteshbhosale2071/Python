def lcmbasedalarm():
    intervals = list(map(int, input(
        "Enter alarm intervals in minutes separated by spaces: "
    ).split()))

    if not intervals or any(interval <= 0 for interval in intervals):
        print("Please enter positive intervals.")
        return

    def find_hcf(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def find_lcm(a, b):
        return (a * b) // find_hcf(a, b)

    common_interval = intervals[0]

    for interval in intervals[1:]:
        common_interval = find_lcm(common_interval, interval)

    print("Alarms will ring together again after:",
          common_interval, "minutes.")

lcmbasedalarm()