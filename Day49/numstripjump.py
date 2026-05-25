def create():
    position = 0

    while position < 20:

        jump = int(input("Enter jump value: "))

        position += jump

        print("Current Position =", position)

    print("You reached the end!")

create()