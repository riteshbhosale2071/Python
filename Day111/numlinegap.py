def numberlinejump():
    start = int(input("Enter the starting number: "))
    jump = int(input("Enter the jump value: "))
    jumps = int(input("Enter the number of jumps: "))

    position = start

    for i in range(jumps):
        position = position + jump

    print("Final Position:", position)

numberlinejump()