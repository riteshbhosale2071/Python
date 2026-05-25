def create():
    beads = input("Enter bead colors separated by space: ").split()

    count = {}

    for i in beads:

        if i in count:
            count[i] += 1

        else:
            count[i] = 1

    print("Beads Count =", count)

create()