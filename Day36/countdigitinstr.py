def find():
    s = input("Enter the string: ")
    count = 0

    for i in s.split():
        if i.isdigit():
            count += 1

    print("Number of digits =", count)

find()