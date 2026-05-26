def create():
    total_weight = 0

    while True:

        weight = int(input("Enter marble weight (0 to stop): "))

        if weight == 0:
            break

        total_weight += weight

    print("Total Marble Weight =", total_weight)

create()