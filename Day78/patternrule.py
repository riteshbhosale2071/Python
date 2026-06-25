def pattern():
    numbers = list(map(int,input("Enter numbers separated by space : ").split()))

    for num in numbers:
        if num % 2 == 0:
            print(f"{num} is even")

        else:
            print(f"{num} is odd")
pattern()