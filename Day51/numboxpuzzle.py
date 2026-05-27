def create():
    rows = int(input("Enter rows: "))
    cols = int(input("Enter columns: "))

    num = 1

    for i in range(rows):

        for j in range(cols):
            print(num, end=" ")

            num += 1

        print()

create()