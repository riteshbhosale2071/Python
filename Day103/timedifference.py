def timedifference():
    h1 = int(input("Enter start hour: "))
    m1 = int(input("Enter start minute: "))
    h2 = int(input("Enter end hour: "))
    m2 = int(input("Enter end minute: "))

    start = h1 * 60 + m1
    end = h2 * 60 + m2

    difference = end - start

    hours = difference // 60
    minutes = difference % 60

    print("Time Difference =", hours, "hours", minutes, "minutes")

timedifference()