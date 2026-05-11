def find():
    sum = 0
    count = 0

    while(True):
        num = int(input("Enter number: "))

        if num == 0:
            break

        sum = sum + num
        count += 1

    avg = sum / count

    print("Sum of all nums is:",sum)
    print("Average of all nums is:",avg)

find()