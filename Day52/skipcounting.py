def count():
    start = int(input("Enter starting number: "))

    end = int(input("Enter ending number: "))
    
    skip = int(input("Enter skip value: "))

    count = 0

    for i in range(start, end + 1, skip):

        print(i)

        count += 1

    print("\nTotal Skips =", count)

count()