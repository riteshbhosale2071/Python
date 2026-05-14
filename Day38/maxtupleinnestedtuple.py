def maxx():
    t = ((1, 2, 3),
     (10, 20, 5),
     (4, 4, 4))

    max_sum = 0
    max_row = ()

    for row in t:
        total = sum(row)

        if total > max_sum:
            max_sum = total
            max_row = row

    print("Row with Maximum Sum:", max_row)
    print("Maximum Sum:", max_sum)

maxx()