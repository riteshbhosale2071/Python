def unit():
    number = int(input("Enter a 3-digit number: "))

    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    print("Hundreds =", hundreds)
    print("Tens =", tens)
    print("Units =", units)

unit()