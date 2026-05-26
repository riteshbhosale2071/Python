def create():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    num = 1

    for i in range(rows):

        temp = []

        for j in range(cols):
            temp.append(num)
            num += 1

        if i % 2 != 0:
            temp.reverse()

        print(temp)

create()