def worktimecalc():
    workers = int(input("Enter number of workers: "))
    time = float(input("Enter time taken by workers (in hours): "))
    new_workers = int(input("Enter new number of workers: "))

    if workers <= 0 or time <= 0 or new_workers <= 0:
        print("Please enter positive values.")
        return

    total_work = workers * time
    new_time = total_work / new_workers

    print("Total Work:", total_work, "worker-hours")
    print("Time required by new workers:", new_time, "hours")

worktimecalc()