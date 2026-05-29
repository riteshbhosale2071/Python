def create():
    maze = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    target = int(input("Enter number to find: "))

    found = False

    for i in range(len(maze)):

        for j in range(len(maze[i])):

            if maze[i][j] == target:

                print("Found at Row", i, "Column", j)

                found = True

    if not found:
        print("Number not found")

create()