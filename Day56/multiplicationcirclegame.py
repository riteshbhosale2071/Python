def game():
    num = int(input("Enter number: "))
    rounds = int(input("Enter rounds: "))

    value = num

    for i in range(rounds):

        print(value, end=" ")

        value *= num

    print()

game()