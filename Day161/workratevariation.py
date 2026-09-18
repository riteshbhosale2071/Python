def workratevariation():
    print("Work-Rate Variation Simulator :")
    print("1. More Workers")
    print("2. Fewer Workers")

    workers = int(input("Enter number of workers: "))
    days = float(input("Enter number of days: "))
    change = int(input("Enter new number of workers: "))

    if workers > 0 and change > 0:
        total_work = workers * days
        new_days = total_work / change

        print("Original workers =", workers)
        print("Original days =", days)
        print("New workers =", change)
        print("New required days =", new_days)

        if change > workers:
            print("More workers reduce the required time.")
        elif change < workers:
            print("Fewer workers increase the required time.")
        else:
            print("Number of workers is unchanged.")
    else:
        print("Number of workers must be greater than zero.")

workratevariation()