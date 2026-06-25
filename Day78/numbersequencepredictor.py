def sequence():
    numbers = list(map(int,input("Enter numbers separated by space : ").split()))

    difference = numbers[1] - numbers[0]
    next_num = numbers[-1] + difference

    print("Next number :",next_num)

sequence()