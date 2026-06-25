def completepattern():
    numbers = list(map(int,input("Enter the pattern by space : ").split()))

    difference = numbers[1] - numbers[0]

    next_num  = numbers[-1] + difference

    print("Complete Pattern")
    print(numbers+[next_num])

completepattern()