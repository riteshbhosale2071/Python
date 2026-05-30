def expand():
    num = int(input("Enter a number: "))

    place = 1

    while num > 0:

        digit = num % 10

        print(digit * place)

        place *= 10
        num //= 10

expand()