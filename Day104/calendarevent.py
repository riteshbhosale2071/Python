def eventduration():
    start = int(input("Enter start hour: "))
    end = int(input("Enter end hour: "))

    duration = end - start
    print("Event Duration =", duration, "hours")

eventduration()