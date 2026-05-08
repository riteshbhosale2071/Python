def user(*values):
    total = 0
    count = 0
    for i in values:
        if i %2 == 0:
            total += i
            count += 1
    print("Aerage of user values is",total/count)

user(10,20,30,40,50)