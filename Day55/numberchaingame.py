def find():
    num = int(input("Enter starting number: "))
    steps = int(input("Enter number of steps: "))

    print("Number Chain:")

    for i in range(steps):

        print(num, end=" -> ")

        num += 1

    print(num)

find()