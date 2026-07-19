def factortree():
    number = int(input("Enter a number: "))
    print("Prime Factors are:")

    i = 2
    while number > 1:
        if number % i == 0:
            print(i)
            number = number // i
        else:
            i += 1

factortree()