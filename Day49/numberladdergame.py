def create():
    num = int(input("Enter starting number: "))

    while num > 0:

        print(num)

        step = int(input("Enter step to climb down: "))

        num = num - step

    print("Game Over")

create()